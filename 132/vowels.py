from typing import Tuple

VOWELS = set('aeiou')


def get_word_max_vowels(text: str) -> Tuple[str, int]:
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    return max(((word, len([char for char in word if char in VOWELS])) for word in text.split()), key=lambda x: x[1])
