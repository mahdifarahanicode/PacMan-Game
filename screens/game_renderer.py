import pygame
from core.config import *
from core.themes import themes
import core.sprites as sprites

def draw_game(screen, state, font, player_rect):

    theme = themes[state.current_level]
    screen.fill(theme["background"])

    # walls
    for w in state.walls:
        pygame.draw.rect(screen, theme["wall"], w)

    for d in state.dots:

        if d["type"] == "normal":

            pygame.draw.rect(
                screen,
                theme["dot"],
                d["rect"]
            )

        else:

            pygame.draw.circle(
            screen,
            (255,120,255),
            d["rect"].center,
            9
        )

            pygame.draw.circle(
                screen,
                (255,255,255),
                d["rect"].center,
                3
        )

    # ghosts
    for g in state.ghosts:

        if state.powered:

            image = sprites.SCARED_GHOST

        else:

            if g["sprite"] == "red":
                image = sprites.RED_GHOST

            elif g["sprite"] == "purple":
                image = sprites.PURPLE_GHOST

            else:
                image = sprites.BLUE_GHOST

        screen.blit(
            image,
            (g["x"], g["y"])
        )

    # player animation
    frame = (pygame.time.get_ticks() // 150) % 2

    if state.powered:

        if frame == 0:
            image = sprites.PACMAN_POWERED_CLOSED
        else:
            image = sprites.PACMAN_POWERED_OPEN

    else:

        if frame == 0:
            image = sprites.PACMAN_CLOSED
        else:
            image = sprites.PACMAN_OPEN


    # Rotate / Flip based on movement direction
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        image = pygame.transform.flip(image, True, False)

    elif keys[pygame.K_UP]:
        image = pygame.transform.rotate(image, -90)

    elif keys[pygame.K_DOWN]:
        image = pygame.transform.rotate(image, 90)

    screen.blit(image, player_rect)

    # HUD
    score_text = font.render(f"Score: {state.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    level_text = font.render(
        f"Level: {state.current_level}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        level_text,
        (WIDTH // 2 - level_text.get_width() // 2, 10)
    )

    lives_text = font.render(
        f"Lives: {state.lives}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        lives_text,
        (WIDTH - lives_text.get_width() - 10, 10)
    )