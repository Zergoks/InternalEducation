from pathlib import Path
from time import sleep
import random
import string


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def list_of_random_strings(amount_of_strings: int) -> list:
    """Генерируем лист с стрингами"""
    result = []
    letters = string.ascii_letters + string.digits
    for time in range(amount_of_strings):
        result.append(''.join(random.choice(letters) for i in range(random.randint(1, 100))))
    return result


def explicit_sleep(time=1):
    """Вынесено в отдельную функцию чтобы было проще рефакторить,
    когда будет понятно решение проблемы"""
    sleep(time)