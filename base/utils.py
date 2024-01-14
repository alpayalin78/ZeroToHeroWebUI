import string
import random


def generate_random_number(limit: int = 5) -> str:
    """
    Generates random Number.

    Args:

    Returns:
        str
    """
    number = ""

    for _ in range(limit):
        digit = random.randint(0, 9)
        number += str(digit)

    return number


def generate_random_text(character_count) -> str:
    """
    Generates random Text.

    Args:
        character_count: defines how many character generated random text will be made of

    Returns:
        str
    """
    if character_count <= 0:
        return "Geçersiz giriş: Pozitif bir karakter sayısı girin."

    letters = string.ascii_letters
    random_text = ''.join(random.choice(letters) for _ in range(character_count))

    return random_text
