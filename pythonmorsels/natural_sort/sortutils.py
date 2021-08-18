import re
from typing import Iterable, Optional, Callable, Union
from functools import singledispatch


# Human sorting method from https://nedbatchelder.com/blog/200712/human_sorting.html

def _tryint(s: str) -> Union[int, str]:
    try:
        return int(s)
    except ValueError:
        return s

@singledispatch
def natural_key(s: str) -> list[Union[str, int]]:
    return [_tryint(str.casefold(c)) for c in re.split('([0-9]+)', s)]


def natural_sort(iterable: Iterable[str],
                 reverse: bool = False,
                 key: Optional[Callable[[str], str]] = None) -> Iterable[str]:
    _key = natural_key if key is None else key
    return sorted(iterable, reverse=reverse, key=_key)
