from typing import Tuple


def magic_tuples(total_value: int, limit_value: int) -> Tuple[int, int]:
    for a in range(limit_value):
        b = total_value - a
        if b < limit_value:
            yield a, b
