from typing import Iterable, Iterator, Any


class loop_tracker:
    EMPTY = object()

    def __init__(self, underlying_iterable: Iterable[Any]):
        self.length = 0  # type: int
        self.empty_accesses = 0  # type: int
        self.underlying = iter(underlying_iterable)
        self.first = self.EMPTY
        self.last = self.EMPTY
        self._next = self.EMPTY
        try:
            self._next = next(self.underlying)
        except StopIteration:
            pass

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self._next is self.EMPTY:
            self.empty_accesses += 1
            raise StopIteration
        else:
            next_value = self._next
        try:
            self._next = next(self.underlying)
        except StopIteration as e:
            self._next = self.EMPTY
        finally:
            self.length += 1
            return next_value

    def is_empty(self):
        return bool(self._next is self.EMPTY)

