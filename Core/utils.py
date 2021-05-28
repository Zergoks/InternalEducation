from pathlib import Path
from time import sleep
import random
import string


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def random_string_mix(string_length):
    """Генерируем стрингу с миксом букв и символов """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(string_length))

def explicit_sleep(time=1):
    """Вынесено в отдельную функцию чтобы было проще рефакторить,
    когда будет понятно решение проблемы"""
    sleep(time)