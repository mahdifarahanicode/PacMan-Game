import os
import sys


def resource_path(relative_path):
    """
    Return the absolute path to bundled resources.
    Works both in development and in a PyInstaller executable.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_data_folder():
    """
    Return the application's writable data folder.

    Windows:
        %LOCALAPPDATA%/PacMan
    """

    if sys.platform.startswith("win"):
        base = os.getenv("LOCALAPPDATA")

        if not base:
            base = os.path.expanduser("~")

    else:
        base = os.path.expanduser("~")

    folder = os.path.join(base, "PacMan")

    os.makedirs(folder, exist_ok=True)

    return folder


def data_path(relative_path=""):
    """
    Build an absolute path inside the application's data folder.
    """

    return os.path.join(get_data_folder(), relative_path)


def ensure_directories():
    """
    Create required folders on first launch.
    """

    os.makedirs(data_path("logs"), exist_ok=True)