import traceback

from core.resource_path import data_path


def log_exception(exc):

    logfile = data_path("logs/crash.log")

    with open(logfile, "a", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        traceback.print_exc(file=f)