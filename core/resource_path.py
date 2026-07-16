import os
import sys


def resource_path(relative_path):
    """
    مسیر فایل‌های داخل برنامه (تصاویر، صداها و ...)
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_data_folder():
    """
    محل ذخیره اطلاعات کاربر
    Windows:
        C:\Users\<User>\AppData\Local\PacMan
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

    return os.path.join(get_data_folder(), relative_path)


def ensure_directories():

    os.makedirs(data_path("logs"), exist_ok=True)