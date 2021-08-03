from typing import Iterable, Iterator, Any


class loop_tracker:
    def __init__(self, underlying_iterable: Iterable[Any]):
        self.length = 0  # type: int
        self.underlying = iter(underlying_iterable)

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
            next_value = next(self.underlying)
            self.length += 1
            return next_value
