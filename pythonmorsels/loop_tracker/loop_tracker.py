import collections.abc
from typing import Iterable, Iterator, Any


class loop_tracker(collections.abc.Iterable):
    EMPTY = object()

    def __init__(self, underlying_iterable: Iterable[Any]):
        self._length = 0  # type: int
        self.empty_accesses = 0  # type: int
        self._underlying = iter(underlying_iterable)
        self._first = self.EMPTY
        self._last = self.EMPTY
        self._cached = self.EMPTY

    def _get_next(self):
        if self._first is self.EMPTY:
            item = next(self._underlying, self.EMPTY)
            self._first = item
        elif self._cached is not self.EMPTY:
            item = self._cached
            self._cached = self.EMPTY
        else:
            item = next(self._underlying, self.EMPTY)
        return item

    @property
    def first(self):
        if self._first is self.EMPTY:
            if self.is_empty():
                raise AttributeError("iterable has no first attribute (it's empty)")
        return self._first

    @property
    def last(self):
        if self._last is self.EMPTY:
            raise AttributeError("no last item yet (no looping performed yet)")
        return self._last

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        item = self._get_next()
        if item is self.EMPTY:
            self.empty_accesses += 1
            return next(self._underlying)
        else:
            self._last = item
            self._length += 1
            return item

    def is_empty(self):
        if self._cached is self.EMPTY:
            self._cached = self._get_next()
            return bool(self._cached is self.EMPTY)
