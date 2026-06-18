import os
import pygame
import sys
import random
from collections import deque
from assets.maps import maps
from core.config import *
from core import sounds
import game.state as state
from game.engine import reset_game
import game.player as player
import game.pathfinding as pathfinding
import screens.menu as menu
import screens.level_complete as level_complete
import screens.gameover as gameover
import screens.hud as hud

from game.ghosts import spawn_ghost, move_ghosts
import core.config as config
from core.levels import *
from core.score import *

pygame.init()
pygame.mixer.init()
sounds.init_sounds()

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 60)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")
clock = pygame.time.Clock()

state.map_data = maps[config.current_level - 1]
state.rows = len(state.map_data)
state.cols = len(state.map_data[0])
state.walls.clear()

for y, row in enumerate(state.map_data):
    for x, cell in enumerate(row):

        if cell == "1":
            state.walls.append(
                pygame.Rect(x * tile, y * tile, tile, tile)
            )

def is_valid_spawn(x, y):
    rect = pygame.Rect(x, y, player_size, player_size)
    return not any(rect.colliderect(w) for w in state.walls)

while True:
    player_x = random.randint(0, WIDTH - player_size)
    player_y = random.randint(0, HEIGHT - player_size)

    if is_valid_spawn(player_x, player_y):
        break

state.player_x = player_x
state.player_y = player_y

state.ghosts = []

for _ in range(levels[current_level]["ghost_count"]):
    g = spawn_ghost()

    if g:
        state.ghosts.append(g)

def handle_movement(x, y):
    keys = pygame.key.get_pressed()

    new_x, new_y = x, y

    if keys[pygame.K_LEFT]:
        new_x -= speed
    if keys[pygame.K_RIGHT]:
        new_x += speed
    if keys[pygame.K_UP]:
        new_y -= speed
    if keys[pygame.K_DOWN]:
        new_y += speed

    rect = pygame.Rect(new_x, new_y, player_size, player_size)

    if any(rect.colliderect(w) for w in state.walls):
        return x, y

    return new_x, new_y

state.dots.clear()

for y in range(state.rows):
    for x in range(state.cols):
        if state.map_data[y][x] == "0":
            state.dots.append(
                pygame.Rect(
                    x * tile + tile//2,
                    y * tile + tile//2,
                    5, 5
                )
            )

highscore = load_highscore()

running = True

while running:

    if player_state == "respawning":
        respawn_timer -= 1

        if respawn_timer <= 0:
            reset_game(current_level)
            player_state = "alive"

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if state.game_state == "menu":

                if event.key == pygame.K_SPACE:
                    sounds.menu_sound.stop()
                    menu_started = False
                    state.game_state = "playing"
                    reset_game(current_level)

            if event.key == pygame.K_r:
                state.game_state = "playing"
                reset_game(current_level, full_reset=True)

    if state.game_state == "menu":

        if not menu_started:
            sounds.menu_sound.play(-1)
            menu_started = True

        menu.draw_menu(
            screen,
            font,
            big_font,
            WIDTH,
            HEIGHT
        )

        pygame.display.flip()
        clock.tick(60)
        continue

    if state.game_state == "level_complete":

        level_complete.draw_level_complete(
            screen,
            font,
            WIDTH,
            HEIGHT,
            current_level,
            score
        )

        pygame.display.flip()

        level_complete_timer -= 1

        if level_complete_timer <= 0:
            current_level += 1
            state.current_level = current_level
            reset_game(current_level)
            state.game_state = "playing"

        clock.tick(60)
        continue

    if state.game_state != "playing":
        screen.fill((0, 0, 0))

        if not menu_music_played:
            sounds.menu_sound.play()
            menu_music_played = True

        gameover.draw_gameover(
            screen,
            font,
            WIDTH,
            HEIGHT,
            state.game_state,
            score,
            highscore
        )

        pygame.display.flip()
        clock.tick(60)
        continue

    state.player_x, state.player_y = handle_movement(state.player_x, state.player_y)
    player_x, player_y = state.player_x, state.player_y

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # eat dots
    for d in state.dots[:]:
        if player_rect.colliderect(d):
            state.dots.remove(d)
            score += 1
            sounds.eat_sound.play()
    
    move_ghosts()

    # render
    screen.fill((0, 0, 0))

    for w in state.walls:
        pygame.draw.rect(screen, (0, 0, 255), w)

    for d in state.dots:
        pygame.draw.rect(screen, (255, 255, 255), d)

    for g in state.ghosts:
        pygame.draw.rect(screen, (255, 0, 0), (g["x"], g["y"], ghost_size, ghost_size))

    pygame.draw.rect(screen, (255, 255, 0), (player_x, player_y, player_size, player_size))

    # collision
    if player_state == "alive":
        for g in state.ghosts:
            if player_rect.colliderect(pygame.Rect(g["x"], g["y"], ghost_size, ghost_size)):
                lives -= 1

                if lives <= 0:
                    save_highscore(score)
                    highscore = load_highscore()
                    sounds.gameover_sound.play()
                    state.game_state = "lose"
                    player_state = "dead"
                
                else:
                    sounds.respawn_sound.play()
                    player_state = "respawning"
                    respawn_timer = 60

                break
    
    if len(state.dots) == 0:

        if current_level < 3:
            state.game_state = "level_complete"
            level_complete_timer = 180   # 3 ثانیه در 60 FPS
            sounds.levelup_sound.play()

        else:
            save_highscore(score)
            highscore = load_highscore()
            sounds.win_sound.play()
            state.game_state = "win"

        hud.draw_hud(
        screen,
        font,
        WIDTH,
        score,
        current_level,
        lives
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()