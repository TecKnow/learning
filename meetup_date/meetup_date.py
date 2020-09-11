import datetime
import calendar
from enum import IntEnum, unique


@unique
class Weekday(IntEnum):
    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)


the_calendar = calendar.Calendar()


def meetup_date(year, month, nth=None, weekday=None):
    cal_iter = the_calendar.itermonthdays2(year, month)
    nth = 4 if nth is None else nth
    if weekday is None:
        #  The default weekday is Thursday.
        weekday = 3
    elif hasattr(weekday, "value"):
        weekday = weekday.value
    target_weekdays = [month_day for month_day, week_day in cal_iter if month_day != 0 and week_day == weekday]
    target_month_day = target_weekdays[nth - 1 if nth > 0 else nth]
    return datetime.date(year, month, target_month_day)
