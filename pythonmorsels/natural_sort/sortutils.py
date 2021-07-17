from typing import Iterable

def natural_sort(iterable : Iterable[str], reverse : bool=False) -> Iterable[str]:
    return sorted(iterable, reverse=reverse, key=str.casefold)