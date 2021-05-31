from pathlib import Path
from time import sleep


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def explicit_sleep(time=1):
    """Вынесено в отдельную функцию чтобы было проще рефакторить,
    когда будет понятно решение проблемы"""
    sleep(time)

def generate_random(amount):
    return [x for x in range(amount)]