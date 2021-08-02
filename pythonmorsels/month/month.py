from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Month:
    __slots__ = tuple("year month".split())
    year: int
    month: int

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}"