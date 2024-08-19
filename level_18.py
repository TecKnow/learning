"""Python challenge level 18: Can you tell the difference?

solution: http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
"""

import tempfile
from pathlib import Path
import logging
import gzip
from difflib import Differ

import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TEMP_DIR = Path(tempfile.gettempdir())

AUTH: tuple[str, str] = ("huge", "file")
URL: str = "http://www.pythonchallenge.com/pc/return/balloons.html"
URL_2: str = "http://www.pythonchallenge.com/pc/return/brightness.html"
# <!-- maybe consider deltas.gz -->

DATA_ARCHIVE_URL: str = "http://www.pythonchallenge.com/pc/return/deltas.gz"
DATA_PATH = TEMP_DIR / "deltas.gz"


def get_deltas_data() -> str:
    """ Returned the decompressed contents of "deltas.gz"

        Download the deltas.gz data file if needed,
        and return the decompressed data"""

    if not DATA_PATH.exists():
        logger.info("Data file not found, downloading.")
        r = requests.get(DATA_ARCHIVE_URL, auth=AUTH, timeout=30)
        DATA_PATH.open('wb').write(r.content)
    else:
        logger.info("Found existing data file")
    return gzip.open(DATA_PATH, 'rt').read()


def deinterlace_deltas_data(deltas_data: str) -> tuple[str, str]:
    """Deinterlace the data from deltas.gz

    The data in deltas.gz is clearly split into two groups,
    a left side and a right side.  Separate them"""
    left_str_list: list[str] = list()
    right_str_list: list[str] = list()
    for delta_line in deltas_data.splitlines():
        left_part, _, right_part = delta_line.partition("   ")
        left_str_list.append(left_part.strip())
        right_str_list.append(right_part.strip())
    return "\n".join(left_str_list), "\n".join(right_str_list)


def create_diff(left_str: str, right_str: str) -> list[str]:
    """ Create a diff of the two text files deinterlaced from deltas.gz"""
    left_str_list = left_str.splitlines()
    right_str_list = right_str.splitlines()
    differ = Differ()

    return differ.compare(left_str_list, right_str_list)


def demux_diff(diff: list[str]) -> tuple[str, str, str]:
    """Separate the lines of the diff into three strings based on label"""

    left_text_list: str = list()
    center_text_list: str = list()
    right_text_list: str = list()

    for line in diff:
        prefix, data = line[0:2], line[2:].strip()
        if prefix == "- ":
            left_text_list.append(data)
        elif prefix == "  ":
            center_text_list.append(data)
        elif prefix == "+ ":
            right_text_list.append(data)
        else:
            logger.error("Found unexpected prefix %s", prefix)

    return (" ".join(elem_list) for elem_list in (
            left_text_list,
            center_text_list,
            right_text_list))


def strings_to_bytes(string_of_hex_values: str) -> bytes:
    """Convert a string of hex values into bytes"""
    return bytes([int(n, 16) for n in string_of_hex_values.split()])


def main_function():
    """ Show the process of solving this problem from scratch"""
    deltas_data = get_deltas_data()
    left_column, right_column = deinterlace_deltas_data(deltas_data)
    diff = create_diff(left_column, right_column)
    left_str, center_str, right_str = demux_diff(diff)
    left_bytes, center_bytes, right_bytes = (
        strings_to_bytes(content)for content in (
            left_str,
            center_str,
            right_str))

    right_path, center_path, left_path = (
        TEMP_DIR / POS for POS in (
            "LEFT CENTER RIGHT". split()))

    right_path.open('wb').write(right_bytes)
    center_path.open('wb').write(center_bytes)
    left_path.open('wb').write(left_bytes)


if __name__ == "__main__":
    main_function()
