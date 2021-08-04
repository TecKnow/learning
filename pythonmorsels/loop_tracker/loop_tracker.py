from typing import Iterable, Iterator, Any


class loop_tracker:
    EMPTY = object()

    def __init__(self, underlying_iterable: Iterable[Any]):
        self.length = 0  # type: int
        self.empty_accesses = 0  # type: int
        self.underlying = iter(underlying_iterable)
        self._first = self.EMPTY
        self._last = self.EMPTY
        self._next = self.EMPTY
        try:
            self._next = next(self.underlying)
            self._first = self._next
        except StopIteration:
            pass

    @property
    def first(self):
        if self._first is self.EMPTY:
            raise AttributeError("iterable has no first attribute (it's empty)")
        return self._first

    @property
    def last(self):
        if self._last is self.EMPTY:
            raise AttributeError("no last item yet (no looping performed yet)")
        return self._last

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self._next is self.EMPTY:
            self.empty_accesses += 1
            raise StopIteration
        else:
            self._last = self._next
        try:
            self._next = next(self.underlying)
        except StopIteration as e:
            self._next = self.EMPTY
        finally:
            self.length += 1
            return self._last

    def is_empty(self):
        return bool(self._next is self.EMPTY)
