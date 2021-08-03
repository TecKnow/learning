import datetime
from calendar import monthrange
from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Month:

    @classmethod
    def from_date(cls, date: datetime.date):
        return cls(date.year, date.month)

    def strftime(self, format_string: str) -> str:
        date_object = datetime.date(self.year, self.month, 1)
        return date_object.strftime(format_string)

    __slots__ = tuple("year month".split())
    year: int
    month: int

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}"

    @property
    def first_day(self):
        return datetime.date(self.year, self.month, 1)

    @property
    def last_day(self):
        num_days = monthrange(self.year, self.month)[1]
        return datetime.date(self.year, self.month, num_days)
