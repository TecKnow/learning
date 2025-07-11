"""Python challenge level 7: smarty

Solution: integrity
"""

import logging
import re
from ast import literal_eval
from pathlib import Path

import png
import requests

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/def/oxygen.html"
PNG_URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"

TMP = Path("/tmp")
PNGFILE_PATH = TMP / "oxygen.png"


def _load_data():
    if not PNGFILE_PATH.exists():
        logger.info("PNG file not found, attempting to download")
        pngfile_obj = PNGFILE_PATH.open("wb")
        pngdata = requests.get(PNG_URL, timeout=30).content
        pngfile_obj.write(pngdata)
        pngfile_obj.close()
    else:
        logger.info("Existing PNG file found")


if __name__ == "__main__":
    next_nothing_re = re.compile(r"Next nothing is (\d+)", flags=re.IGNORECASE)
    _load_data()
    r = png.Reader(str(PNGFILE_PATH))
    image_data = r.read()
    print(image_data)
    for row_number, row in enumerate(image_data[2]):
        # The encoded rows are 43..51 but I think we only need one of them.
        if row_number == 43:
            PREVIOUS_NUMBER = None
            result = list()
            for number in row:
                if number <= 127 and number != PREVIOUS_NUMBER:
                    result.append(number)
                    PREVIOUS_NUMBER = number
    RESULT_STRING = (''.join([chr(x) for x in result]))
    print(RESULT_STRING)
    match = re.search(r"(\[.+?\])", RESULT_STRING)
    literal_string = match.group(1)
    ordinal_list = literal_eval(literal_string)
    """Based on the previous steps in the solution these are all ASCII
    characters but some are in the non-printable range.
    The printable alphabet is between 32 and 126

    My frist thought was to assume the values < 32 were negatives, but that 
    doesn't work.  But what if I just assume the values < 100 are missing
    their most significant digit?"""
    fixed_ordinals = [x if x > 100 else x+100 for x in ordinal_list]
    NEXT_LEVEL = ''.join([chr(x) for x in fixed_ordinals])
    print(NEXT_LEVEL)
