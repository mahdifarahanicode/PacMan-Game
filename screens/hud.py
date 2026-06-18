import pygame

def draw_hud(screen, font, width, score, current_level, lives):

    # Score (top-left)
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

    # Level (top-center)
    level_text = font.render(
        f"Level: {current_level}",
        True,
        (255, 255, 255)
    )
    screen.blit(
        level_text,
        (
            width // 2 - level_text.get_width() // 2,
            10
        )
    )

    # Lives (top-right)
    lives_text = font.render(
        f"Lives: {lives}",
        True,
        (255, 255, 255)
    )
    screen.blit(
        lives_text,
        (
            width - lives_text.get_width() - 10,
            10
        )
    )