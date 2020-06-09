from itertools import chain, islice, repeat

_DEFAULT_FILLVALUE = object()


def chunked(iterable, n, *, fill=_DEFAULT_FILLVALUE):
    _EOL = object()
    iterator = iter(iterable)
    padded_iterator = iterator if fill is _DEFAULT_FILLVALUE else chain(iterator, repeat(fill))
    while (currentValue := next(iterator, _EOL)) is not _EOL:
        restored_iterator = chain((currentValue,), padded_iterator)
        yield islice(restored_iterator, n)
    return
