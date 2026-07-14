import pygame

from core.config import player_size, ghost_size
from core.resource_path import resource_path


def load_image(path, size):

    image = pygame.image.load(
        resource_path(path)
    ).convert_alpha()

    return pygame.transform.scale(image, (size, size))

PACMAN_CLOSED = None
PACMAN_OPEN = None
PACMAN_POWERED_CLOSED = None
PACMAN_POWERED_OPEN = None

RED_GHOST = None
PURPLE_GHOST = None
BLUE_GHOST = None
SCARED_GHOST = None

def load_sprites():

    global PACMAN_CLOSED
    global PACMAN_OPEN
    global PACMAN_POWERED_CLOSED
    global PACMAN_POWERED_OPEN

    global RED_GHOST
    global PURPLE_GHOST
    global BLUE_GHOST
    global SCARED_GHOST

    PACMAN_CLOSED = load_image(
        "assets/images/pacman/closed.png",
        player_size
    )

    PACMAN_OPEN = load_image(
        "assets/images/pacman/left_open.png",
        player_size
    )

    PACMAN_POWERED_CLOSED = load_image(
        "assets/images/pacman/powered_closed.png",
        player_size
    )

    PACMAN_POWERED_OPEN = load_image(
        "assets/images/pacman/powered_left_open.png",
        player_size
    )

    RED_GHOST = load_image(
        "assets/images/ghosts/red_ghost.png",
        ghost_size
    )

    PURPLE_GHOST = load_image(
        "assets/images/ghosts/purple_ghost.png",
        ghost_size
    )

    BLUE_GHOST = load_image(
        "assets/images/ghosts/blue_ghost.png",
        ghost_size
    )

    SCARED_GHOST = load_image(
        "assets/images/ghosts/scared_ghost.png",
        ghost_size
    )