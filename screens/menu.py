import pygame

def draw_menu(screen, font, big_font, small_font, width, height):

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

    info1 = small_font.render(
    "6 Progressive Levels",
    True,
    (220, 220, 220)
    )

    info2 = small_font.render(
        "Levels 1-2 : Random Ghosts",
        True,
        (170, 170, 170)
    )

    info3 = small_font.render(
        "Levels 3-4 : Mixed AI",
        True,
        (170, 170, 170)
    )

    info4 = small_font.render(
        "Levels 5-6 : Smart Ghosts",
        True,
        (170, 170, 170)
    )

    info5 = small_font.render(
        "Power Pellets let you eat ghosts for 5 seconds",
        True,
        (255, 180, 180)
    )

    esc_text = small_font.render(
        "ESC : Pause",
        True,
        (170,170,170)
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
        info1,
        (
            width // 2 - info1.get_width() // 2,
            height // 2 + 55
        )
    )

    screen.blit(
        info2,
        (
            width // 2 - info2.get_width() // 2,
            height // 2 + 85
        )
    )

    screen.blit(
        info3,
        (
            width // 2 - info3.get_width() // 2,
            height // 2 + 110
        )
    )

    screen.blit(
        info4,
        (
            width // 2 - info4.get_width() // 2,
            height // 2 + 135
        )
    )

    screen.blit(
        info5,
        (
            width // 2 - info5.get_width() // 2,
            height // 2 + 170
        )
    )

    screen.blit(
        esc_text,
        (
            width // 2 - esc_text.get_width() // 2,
            height // 2 + 200
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