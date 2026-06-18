import pygame

def draw_menu(screen, font, big_font, width, height):

    screen.fill((0, 0, 0))

    title_text = big_font.render(
        "PACMAN",
        True,
        (255, 255, 0)
    )

    start_text = font.render(
        "Press SPACE To Start",
        True,
        (255, 255, 255)
    )

    author_text = font.render(
        "Made By Mahdi Farahani",
        True,
        (150, 150, 150)
    )

    thanks_text = font.render(
        "Thanks For Playing This :)",
        True,
        (150, 150, 150)
    )

    screen.blit(
        title_text,
        (
            width // 2 - title_text.get_width() // 2,
            height // 3
        )
    )

    screen.blit(
        start_text,
        (
            width // 2 - start_text.get_width() // 2,
            height // 2
        )
    )

    screen.blit(
        author_text,
        (
            width - author_text.get_width() - 20,
            height - 60
        )
    )

    screen.blit(
        thanks_text,
        (
            width - thanks_text.get_width() - 20,
            height - 30
        )
    )