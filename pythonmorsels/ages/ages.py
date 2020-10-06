from datetime import datetime, date
from fractions import Fraction

DATE_FORMAT_STRING = "%Y-%m-%d"


def _leap_day_between(first: date, second: date) -> bool:
    if first > second:
        first, second = second, first
    if first.month <= 2:
        try:
            first.replace(month=2, day=29)
        except ValueError:
            return False
    else:
        try:
            second.replace(month=2, day=29)
        except ValueError:
            return False
    return True


def _leap_day_safe_replace(previous_date: date = None, year: int = None, month: int = None, day: int = None) -> date:
    year = year if year is not None else previous_date.year
    month = month if month is not None else previous_date.month
    day = day if day is not None else previous_date.day
    try:
        new_date = previous_date.replace(year=year, month=month, day=day)
    except ValueError:
        new_date = previous_date.replace(year=year, month=3, day=1)
    return new_date


def is_over(age: int, birthday: str):
    today = date.today()
    cutoff_year = today.year - age
    cutoff_date = _leap_day_safe_replace(today, year=cutoff_year)
    birthday_date = datetime.strptime(birthday, DATE_FORMAT_STRING).date()
    return birthday_date < cutoff_date


def get_age(birthday: str, exact: bool = False) -> int:
    today = date.today()
    birthday_date = datetime.strptime(birthday, DATE_FORMAT_STRING).date()
    calendar_age = today.year - birthday_date.year
    birthday_passed_this_year = False if (birthday_date.month, birthday_date.day) > (today.month, today.day) else True
    if not birthday_passed_this_year:
        calendar_age -= 1
    if not exact:
        return calendar_age
    previous_birthday_year = today.year if birthday_passed_this_year else today.year - 1
    previous_birthday_date = _leap_day_safe_replace(birthday_date, year=previous_birthday_year)
    days_since_previous_birthday = today - previous_birthday_date
    long_year = _leap_day_between(previous_birthday_date, today)
    days_this_year = 365 if not long_year else 366
    age_fraction = calendar_age + Fraction(days_since_previous_birthday.days, days_this_year)
    return age_fraction
