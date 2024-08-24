"""Python challenge level 3: re

Solution:  linkedlist

To see the solutions to the previous level, replace pc with pcc,
i.e. go to: http://www.pythonchallenge.com/pcc/def/equality.html

Join us on IRC: irc.freenode.net #pythonchallenge
"""

import re
from fetch_data import get_data


URL: str = "http://www.pythonchallenge.com/pc/def/equality.html"


def bodyguards(data: str) -> str:
    bodybuard_re = re.compile(
        r"(?<![A-Z])[A-Z]{3}([^A-Z])[A-Z]{3}(?![A-Z])", flags=re.DOTALL)
    return bodybuard_re.findall(data)


if __name__ == "__main__":
    data = get_data(URL)
    results = bodyguards(data)
    print(results)
