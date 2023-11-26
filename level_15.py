"""Python challenge level 15: whom?

Solution: mozart"""

import logging
import calendar

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/uzi.html"

candidate_years = list()

for missing_digits in range(100):
    candidate_year = int(f"1{missing_digits}6")
    if (calendar.isleap(candidate_year)
            and calendar.monthrange(
                candidate_year,
                1)[0] == calendar.THURSDAY):
        candidate_years.append(candidate_year)
print(candidate_years)
