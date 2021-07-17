from typing import Iterable, Optional, Callable


def natural_sort(iterable: Iterable[str],
                 reverse: bool = False,
                 key: Optional[Callable[[str], str]] = None) -> Iterable[str]:
    _key = natural_key if key is None else key
    return sorted(iterable, reverse=reverse, key=_key)


def natural_key(item: str) -> str:
    return str.casefold(item)