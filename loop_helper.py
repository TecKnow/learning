from typing import Any
from dataclasses import dataclass


@dataclass
class LoopingInfo:
    is_first: bool
    index: int
    current: Any
    previous: Any = None


EXHAUSTED = object()


def loop_helper(iterable, previous_default = None):
    first = True
    previous = previous_default
    for count, item in enumerate(iterable):
        yield item, LoopingInfo(first, count, item, previous)
        first = False
        previous = item
