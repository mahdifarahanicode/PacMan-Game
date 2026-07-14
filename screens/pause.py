import pygame


def draw_pause(screen, font, big_font, width, height, state):

    overlay = pygame.Surface((width, height))
    overlay.set_alpha(170)
    overlay.fill((0, 0, 0))

    screen.blit(overlay, (0, 0))

    title = big_font.render(
        "GAME PAUSED",
        True,
        (255, 255, 0)
    )

    screen.blit(
        title,
        (
            width // 2 - title.get_width() // 2,
            120
        )
    )

    for i, option in enumerate(state.pause_options):

        color = (
            (255, 255, 0)
            if i == state.pause_index
            else (220, 220, 220)
        )

        text = font.render(option, True, color)

        screen.blit(
            text,
            (
                width // 2 - text.get_width() // 2,
                230 + i * 50
            )
        )