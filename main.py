import pygame
import sys
import random

from assets.maps import maps
from core.config import *
from core import sounds
import core.config as config

from game.game_state import GameState
state = GameState()

from game.engine import reset_game
from game.ghosts import spawn_ghost, move_ghosts
from core.levels import levels
from core.score import load_highscore, save_highscore

import screens.pause as pause
import screens.menu as menu
import screens.level_complete as level_complete
import screens.gameover as gameover
import screens.hud as hud
import screens.game_renderer as renderer

# ================= INIT =================
pygame.init()
pygame.mixer.init()
sounds.init_sounds()

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

from core.sprites import load_sprites

load_sprites()

clock = pygame.time.Clock()

# ================= MAP INIT =================
state.map_data = maps[state.current_level - 1]
state.rows = len(state.map_data)
state.cols = len(state.map_data[0])

state.walls.clear()

for y, row in enumerate(state.map_data):
    for x, cell in enumerate(row):
        if cell == "1":
            state.walls.append(
                pygame.Rect(x * tile, y * tile, tile, tile)
            )

# ================= PLAYER SPAWN =================
def is_valid_spawn(x, y):
    rect = pygame.Rect(x, y, player_size, player_size)
    return not any(rect.colliderect(w) for w in state.walls)


while True:
    px = random.randint(0, WIDTH - player_size)
    py = random.randint(0, HEIGHT - player_size)

    if is_valid_spawn(px, py):
        break

state.player_x = px
state.player_y = py

# ================= GHOSTS =================
state.ghosts = []

for _ in range(levels[state.current_level]["ghost_count"]):
    g = spawn_ghost(state)
    if g:
        state.ghosts.append(g)

# ================= DOTS =================
state.dots.clear()

dot_size = 10

for y in range(state.rows):
    for x in range(state.cols):

        if state.map_data[y][x] == "0":

            state.dots.append({

                "rect": pygame.Rect(
                    x * tile + tile // 2 - dot_size // 2,
                    y * tile + tile // 2 - dot_size // 2,
                    dot_size,
                    dot_size
                ),

                "type": "normal"

            })

# انتخاب دو پاور دات
if len(state.dots) >= 2:

    for dot in random.sample(state.dots, 2):
        dot["type"] = "power"

# ================= UTIL =================
def handle_movement(x, y):
    keys = pygame.key.get_pressed()

    nx, ny = x, y

    if keys[pygame.K_LEFT]:
        nx -= speed
    if keys[pygame.K_RIGHT]:
        nx += speed
    if keys[pygame.K_UP]:
        ny -= speed
    if keys[pygame.K_DOWN]:
        ny += speed

    rect = pygame.Rect(nx, ny, player_size, player_size)

    if any(rect.colliderect(w) for w in state.walls):
        return x, y

    return nx, ny

highscore = load_highscore()
running = True

# ================= GAME LOOP =================
while running:

    player_rect = pygame.Rect(
            state.player_x,
            state.player_y,
            player_size,
            player_size
    )
    
    # ---------- input ----------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # ---------- Pause ----------
            if event.key == pygame.K_ESCAPE:

                if state.game_state == "playing":
                    state.pause_index = 0
                    state.game_state = "pause"

                elif state.game_state == "pause":
                    state.game_state = "playing"

            if state.game_state == "pause":

                if event.key == pygame.K_UP:

                    state.pause_index = (
                        state.pause_index - 1
                    ) % len(state.pause_options)

                elif event.key == pygame.K_DOWN:

                    state.pause_index = (
                        state.pause_index + 1
                    ) % len(state.pause_options)

                elif event.key == pygame.K_RETURN:

                    option = state.pause_options[state.pause_index]

                    if option == "Resume":

                        state.game_state = "playing"

                    elif option == "Restart Level":

                        reset_game(
                            state,
                            state.current_level,
                            reset_dots=True
                        )

                        state.game_state = "playing"

                    elif option == "Main Menu":

                        state.game_state = "menu"
                        state.pause_index = 0

                    elif option == "Quit":

                        running = False

            if state.game_state == "menu":
                if event.key == pygame.K_SPACE:
                    sounds.menu_sound.stop()
                    state.menu_started = False
                    state.game_state = "playing"
                    reset_game(state, state.current_level)

            if event.key == pygame.K_r:
                state.game_state = "playing"
                reset_game(state, state.current_level, full_reset=True)

    # ---------- respawn ----------
    if state.player_state == "respawning":
        state.respawn_timer -= 1

        if state.respawn_timer <= 0:
            reset_game(
                state,
                state.current_level,
                reset_dots=False
            )
            state.player_state = "alive"

    # ================= MENU =================
    if state.game_state == "menu":

        if not state.menu_started:
            sounds.menu_sound.play(-1)
            state.menu_started = True

        menu.draw_menu(
            screen,
            font,
            big_font,
            small_font,
            WIDTH,
            HEIGHT
        )

        pygame.display.flip()
        clock.tick(60)
        continue

    # ================= LEVEL COMPLETE =================
    if state.game_state == "level_complete":

        level_complete.draw_level_complete(
            screen,
            font,
            WIDTH,
            HEIGHT,
            state.current_level,
            state.score
        )

        pygame.display.flip()

        state.level_complete_timer -= 1

        if state.level_complete_timer <= 0:
            state.current_level += 1
            reset_game(state, state.current_level)
            state.game_state = "playing"

        clock.tick(60)
        continue

    # ================= GAME OVER / WIN =================
    if state.game_state in ("win", "lose"):

        screen.fill((0, 0, 0))

        if not state.menu_music_played:
            sounds.menu_sound.play()
            state.menu_music_played = True

        gameover.draw_gameover(
            screen,
            font,
            WIDTH,
            HEIGHT,
            state.game_state,
            state.score,
            highscore
        )

        pygame.display.flip()
        clock.tick(60)
        continue

    # ================= GAME LOGIC =================
    if state.game_state == "pause":

        renderer.draw_game(
            screen,
            state,
            font,
            player_rect
        )

        pause.draw_pause(
            screen,
            font,
            big_font,
            WIDTH,
            HEIGHT,
            state
        )

        pygame.display.flip()
        clock.tick(60)
        continue

    state.player_x, state.player_y = handle_movement(
        state.player_x,
        state.player_y
    )

    player_rect = pygame.Rect(
        state.player_x,
        state.player_y,
        player_size,
        player_size
    )

    # eat dots
    # eat dots (FIXED)
    new_dots = []

    for d in state.dots:

        if player_rect.colliderect(d["rect"]):

            state.score += 1
            sounds.eat_sound.play()

            if d["type"] == "power":
                state.powered = True
                state.power_timer = pygame.time.get_ticks() + POWER_DURATION

        else:

            new_dots.append(d)

    state.dots = new_dots

    # 5 second power    
    if state.powered and pygame.time.get_ticks() >= state.power_timer:
        state.powered = False

    move_ghosts(state)


    # collision
    if state.player_state == "alive":

        remaining_ghosts = []

        for g in state.ghosts:

            ghost_rect = pygame.Rect(
                int(g["x"]),
                int(g["y"]),
                ghost_size,
                ghost_size
            )

            if player_rect.colliderect(ghost_rect):

                # Pac-Man powered -> Ghost eaten
                if state.powered:

                    state.score += 200
                    sounds.eat_sound.play()

                    # Ghost حذف می‌شود
                    continue

                # Ghost kills player
                else:

                    state.lives -= 1

                    if state.lives <= 0:
                        save_highscore(state.score)
                        highscore = load_highscore()
                        sounds.gameover_sound.play()
                        state.game_state = "lose"
                        state.player_state = "dead"

                    else:
                        sounds.respawn_sound.play()
                        state.player_state = "respawning"
                        state.respawn_timer = 60

                    break

            remaining_ghosts.append(g)

        state.ghosts = remaining_ghosts

    # level clear
    if len(state.dots) == 0:

        if state.current_level < len(levels):
            state.game_state = "level_complete"
            state.level_complete_timer = 180
            sounds.levelup_sound.play()

        else:
            save_highscore(state.score)
            highscore = load_highscore()
            sounds.win_sound.play()
            state.game_state = "win"

    # ================= RENDER =================
    renderer.draw_game(
        screen,
        state,
        font,
        player_rect
    )
        
    if state.game_state == "pause":

        pause.draw_pause(
            screen,
            font,
            big_font,
            WIDTH,
            HEIGHT,
            state
        )

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()