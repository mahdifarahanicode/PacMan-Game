import pygame
from core.resource_path import resource_path

eat_sound = None
respawn_sound = None
gameover_sound = None
levelup_sound = None
menu_sound = None
win_sound = None
upgrade_sound = None


def init_sounds():
    global eat_sound, respawn_sound, gameover_sound
    global levelup_sound, menu_sound, win_sound, upgrade_sound

    eat_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/eat.wav")
    )
    respawn_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/respawn.wav")
    )
    gameover_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/gameover.wav")
    )
    levelup_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/levelup.wav")
    )
    menu_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/menu.wav")
    )
    win_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/win.wav")
    )
    upgrade_sound = pygame.mixer.Sound(
        resource_path("assets/sounds/upgrade.wav")
    )