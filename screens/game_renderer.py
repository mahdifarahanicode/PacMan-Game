import pygame
from core.config import *

def draw_game(screen, state, font, player_rect):

    screen.fill((0, 0, 0))

    # walls
    for w in state.walls:
        pygame.draw.rect(screen, (0, 0, 255), w)

    # dots
    for d in state.dots:
        pygame.draw.rect(screen, (255, 255, 255), d)

    # ghosts
    for g in state.ghosts:
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (g["x"], g["y"], ghost_size, ghost_size)
        )

    # player
    pygame.draw.rect(
        screen,
        (255, 255, 0),
        player_rect
    )

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