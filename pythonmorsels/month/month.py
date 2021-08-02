from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return (self.year, self.month) == (other.year, other.month)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return (self.year, self.month) < (other.year, other.month)
