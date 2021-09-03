import datetime
from calendar import monthrange
from dataclasses import dataclass
from functools import total_ordering
from math import trunc


@total_ordering
@dataclass(frozen=True)
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

    def __eq__(self, rhs):
        if isinstance(rhs, self.__class__):
            return (self.year, self.month) == (rhs.year, rhs.month)
        else:
            return NotImplemented

    def __gt__(self, rhs):
        if isinstance(rhs, self.__class__):
            return (self.year, self.month) > (rhs.year, rhs.month)
        else:
            return NotImplemented

    def __add__(self, rhs):
        if isinstance(rhs, MonthDelta):
            total_months = self.year * 12 + self.month + rhs.months
            target_year, target_month = divmod(total_months - 1, 12)
            return self.__class__(target_year, target_month + 1)
        else:
            return NotImplemented

    def __sub__(self, rhs):
        if isinstance(rhs, self.__class__):
            self_months = self.year * 12 + self.month
            rhs_months = rhs.year * 12 + rhs.month
            target_months = self_months - rhs_months
            return MonthDelta(target_months)
        elif isinstance(rhs, MonthDelta):
            self_months = self.year * 12 + self.month
            target_months = self_months - rhs.months
            target_year, target_month = divmod(target_months - 1, 12)
            return self.__class__(target_year, target_month + 1)
        else:
            return NotImplemented

    def __format__(self, format_spec):
        return self.first_day.__format__(format_spec)


@total_ordering
@dataclass(frozen=True)
class MonthDelta:
    __slots__ = ("months",)
    months: int

    def __eq__(self, rhs):
        if isinstance(rhs, self.__class__):
            return self.months == rhs.months
        else:
            return NotImplemented

    def __gt__(self, rhs):
        if isinstance(rhs, self.__class__):
            return self.months > rhs.months
        else:
            return NotImplemented

    def __add__(self, rhs):
        if isinstance(rhs, self.__class__):
            return self.__class__(months=(self.months + rhs.months))
        elif isinstance(rhs, Month):
            rhs_months = rhs.year * 12 + rhs.month
            target_months = rhs_months + self.months
            target_year, target_month = divmod(target_months-1, 12)
            return Month(target_year, target_month+1)
        else:
            return NotImplemented

    def __sub__(self, rhs):
        if not isinstance(rhs, self.__class__):
            return NotImplemented
        if isinstance(rhs, self.__class__):
            return self.__class__(months=(self.months - rhs.months))

    def __truediv__(self, rhs):
        if isinstance(rhs, self.__class__):
            return self.months / rhs.months
        else:
            return NotImplemented

    def __floordiv__(self, rhs):
        if isinstance(rhs, self.__class__):
            return self.months // rhs.months
        elif isinstance(rhs, int):
            return self.__class__(months=(self.months // rhs))
        else:
            return NotImplemented

    def __mul__(self, rhs):
        if isinstance(rhs, int):
            return self.__class__(months=(rhs * self.months))
        else:
            return NotImplemented

    __rmul__ = __mul__

    def __mod__(self, rhs):
        if isinstance(rhs, self.__class__):
            return self.months % rhs.months
        elif isinstance(rhs, int):
            return self.__class__(months=(self.months % rhs))
        else:
            return NotImplemented

    def __neg__(self):
        return self.__class__(months=-self.months)


if __name__ == "__main__":
    python2_eol = Month(2020, 1)
    python2_release = Month(2000, 10)
    python2_lifetime = MonthDelta(231)
    print(python2_eol - MonthDelta(4), Month(2019, 9))
