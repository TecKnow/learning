from typing import Any
from dataclasses import dataclass
from itertools import chain

EXHAUSTED = object()


@dataclass
class LoopingInfo:
    is_first: bool
    index: int
    current: Any
    previous: Any = None
    is_last: bool = False
    next: Any = None


def loop_helper(iterable, previous_default=None, next_default=None):
    chained = chain(iterable, (EXHAUSTED,))
    enumeration = enumerate(chained)
    previous_count, previous_item = -2, None
    current_count, current_item = -1, previous_default
    next_count, next_item = next(enumeration)
    first = True
    last = bool(next_item is EXHAUSTED)
    while True:
        if next_item is EXHAUSTED:
            return
        previous_count, previous_item = current_count, current_item
        current_count, current_item = next_count, next_item
        next_count, next_item = next(enumeration)
        last = bool(next_item is EXHAUSTED)
        yield current_item, LoopingInfo(first, current_count, current_item, previous_item, last,
                                        next_item if next_item is not EXHAUSTED else next_default)
        first = False
