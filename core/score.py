import os

from core.resource_path import data_path

SCORE_FILE = data_path("highscore.txt")


def load_highscore():

    if not os.path.exists(SCORE_FILE):

        with open(SCORE_FILE, "w", encoding="utf-8") as f:
            f.write("0")

        return 0

    try:

        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())

    except (ValueError, OSError):

        with open(SCORE_FILE, "w", encoding="utf-8") as f:
            f.write("0")

        return 0


def save_highscore(score):

    current_highscore = load_highscore()

    if score > current_highscore:

        with open(SCORE_FILE, "w", encoding="utf-8") as f:
            f.write(str(score))