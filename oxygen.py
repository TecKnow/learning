import requests
from pathlib import Path
import logging
import re
import png
from ast import literal_eval


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/def/oxygen.html"
PNG_URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"

TMP = Path("/tmp")
PNGFILE_PATH = TMP / "oxygen.png"


def _load_data():
    if not PNGFILE_PATH.exists():
        logger.info("PNG file not found, attempting to download")
        PNGFILE_OBJ = PNGFILE_PATH.open("wb")
        PNGDATA = requests.get(PNG_URL).content
        PNGFILE_OBJ.write(PNGDATA)
        PNGFILE_OBJ.close()
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
            previous_number = None
            result = list()
            for number in row:
                if number <= 127 and number != previous_number:
                    result.append(number)
                    previous_number = number
    result_string = (''.join([chr(x) for x in result]))
    print(result_string)
    match = re.search(r"(\[.+?\])", result_string)
    literal_string = match.group(1)
    ordinal_list = literal_eval(literal_string)
    # Based on the previous steps in the solution these are all ASCII characters
    # but some are in the non-printable range.  The printable alphabet is between 32 and 126 
    # 
    # My frist thought was to assume the values < 32 were negatives, but that doesn't work.
    # But what if I just assume the values < 100 are missing their most significant digit?
    fixed_ordinals = [x if x > 100 else x+100 for x in ordinal_list]
    next_level = ''.join([chr(x) for x in fixed_ordinals])
    print(next_level)