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
        if not isinstance(rhs, self.__class__):
            return NotImplemented
        return (self.year, self.month) == (rhs.year, rhs.month)

    def __gt__(self, rhs):
        if not isinstance(rhs, self.__class__):
            return NotImplemented
        return (self.year, self.month) > (rhs.year, rhs.month)

    def __add__(self, rhs):
        if not isinstance(rhs, MonthDelta):
            return NotImplemented
        if isinstance(rhs, MonthDelta):
            delta_years = trunc(rhs.months / 12)
            delta_months = rhs.months - (12 * delta_years)
            target_year = self.year + delta_years
            target_month = self.month + delta_months
            if target_month > 12:
                target_year += 1
                target_month -= 12

            return self.__class__(target_year, target_month)

    def __sub__(self, rhs):
        if not isinstance(rhs, (self.__class__, MonthDelta)):
            return NotImplemented
        if isinstance(rhs, self.__class__):
            delta_months = self.month - rhs.month
            delta_years = self.year - rhs.year
            total_month_delta = delta_years * 12 + delta_months
            return MonthDelta(total_month_delta)
        if isinstance(rhs, MonthDelta):
            delta_years = trunc(rhs.months / 12)
            delta_months = rhs.months - (12 * delta_years)
            target_year = self.year - delta_years
            target_month = self.month - delta_months
            if target_month <= 0:
                target_year -= 1
                target_month += 12
            return self.__class__(target_year, target_month)


@total_ordering
@dataclass(frozen=True)
class MonthDelta:
    __slots__ = ("months",)
    months: int

    def __eq__(self, rhs):
        if not isinstance(rhs, self.__class__):
            return NotImplemented
        return self.months == rhs.months

    def __gt__(self, rhs):
        if not isinstance(rhs, self.__class__):
            return NotImplemented
        return self.months > rhs.months

    def __add__(self, rhs):
        if not isinstance(rhs, (self.__class__, Month)):
            return NotImplemented
        elif isinstance(rhs, self.__class__):
            return self.__class__(months=(self.months + rhs.months))
        elif isinstance(rhs, Month):
            delta_years = trunc(self.months / 12)
            delta_months = self.months - (delta_years * 12)
            target_year = rhs.year + delta_years
            target_month = rhs.month + delta_months
            return Month(target_year, target_month)

    def __sub__(self, rhs):
        if not isinstance(rhs, self.__class__):
            return NotImplemented
        if isinstance(rhs, self.__class__):
            return self.__class__(months=(self.months - rhs.months))


if __name__ == "__main__":
    python2_eol = Month(2020, 1)
    python2_release = Month(2000, 10)
    python2_lifetime = MonthDelta(231)
    print(python2_eol - MonthDelta(4), Month(2019, 9))
