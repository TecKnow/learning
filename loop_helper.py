from dataclasses import dataclass


@dataclass
class LoopingInfo:
    is_first: bool
    index: int


EXHAUSTED = object()


def loop_helper(iterable):
    first = True
    for count, item in enumerate(iterable):
        yield item, LoopingInfo(first, count)
        first = False
