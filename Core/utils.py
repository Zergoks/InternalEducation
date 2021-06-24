import random
import string
from pathlib import Path
from time import sleep


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def list_of_random_strings(amount_of_strings: int) -> list:
    """Generate list with string of ascii_letters+digits"""
    result = []
    letters = string.ascii_letters + string.digits
    for time in range(amount_of_strings):
        result.append(
            "".join(random.choice(letters) for i in range(random.randint(1, 100))),
        )
    return result


def explicit_sleep(time=1):
    """Used as reference for issue with waiting for element to be clickable.
    Look at github:
    Having time. sleep() for debugging in the merged project code - not good practice #11"""
    sleep(time)
