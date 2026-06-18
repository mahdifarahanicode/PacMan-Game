import pygame

def draw_level_complete(
    screen,
    font,
    width,
    height,
    current_level,
    score
):

    screen.fill((0, 0, 0))

    title_text = font.render(
        f"Level {current_level} Complete!",
        True,
        (0, 255, 0)
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    next_level_text = font.render(
        f"Next Level: {current_level + 1}",
        True,
        (255, 255, 0)
    )

    screen.blit(
        title_text,
        (
            width // 2 - title_text.get_width() // 2,
            height // 2 - 60
        )
    )

    screen.blit(
        score_text,
        (
            width // 2 - score_text.get_width() // 2,
            height // 2
        )
    )

    screen.blit(
        next_level_text,
        (
            width // 2 - next_level_text.get_width() // 2,
            height // 2 + 60
        )
    )