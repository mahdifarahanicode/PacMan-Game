import pygame
from core.config import *
from core.themes import themes

def draw_game(screen, state, font, player_rect):

    theme = themes[state.current_level]
    screen.fill(theme["background"])

    # walls
    for w in state.walls:
        pygame.draw.rect(screen, theme["wall"], w)

    # dots
    for d in state.dots:
        pygame.draw.rect(screen, theme["dot"], d)

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