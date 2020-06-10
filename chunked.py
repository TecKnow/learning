from itertools import chain, islice, repeat
from typing import Any, Iterable, Iterator

_DEFAULT_FILL_VALUE = object()


def chunked(iterable: Iterable[Any], n: int, *, fill: Any = _DEFAULT_FILL_VALUE) -> Iterator[Iterator[Any]]:
    _EOL = object()
    iterator = iter(iterable)
    padded_iterator = iterator if fill is _DEFAULT_FILL_VALUE else chain(iterator, repeat(fill))
    while (currentValue := next(iterator, _EOL)) is not _EOL:
        restored_iterator = chain((currentValue,), padded_iterator)
        yield islice(restored_iterator, n)
    return
