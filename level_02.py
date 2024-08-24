"""Python challenge level 2: ocr

Solution:  equality

General tips:
*  Use the hint.  They are helpful, most of the times.
*  Investigate the data given to you.
*  Avoid looking for spoilers.

Forums: http://www.pythonchallenge.com/forums, read before you post.
IRC: irc.freenode.net #pythonchallenge

To see the solutions to the previous level, replace pc with pcc,
i.e. go to http://www.pythonchallenge/pcc/dev/ocr.html
"""

from collections import Counter

from fetch_data import get_data

URL: str = "http://www.pythonchallenge.com/pc/def/ocr.html"


def count_characters(data: str) -> Counter:
    frequencies = Counter(data)
    return frequencies


if __name__ == "__main__":
    data = get_data(URL)
    frequencies = count_characters(data)
    print(frequencies.most_common())
