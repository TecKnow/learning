"""Python challenge level 6: Now there are pairs

Solution: oxygen
Distractors : hockey

hockey text:
it's in the air.  look at the letters.
"""

import logging
import re
import zipfile
from pathlib import Path

import requests

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/def/channel.html"
ZIP_URL = "http://www.pythonchallenge.com/pc/def/channel.zip"

TMP = Path("/tmp")
ZIPFILE_PATH = TMP / "channel.zip"


def _load_data():
    if not ZIPFILE_PATH.exists():
        logger.info("Zipfile not found, attempting to download")
        zipfile_obj = ZIPFILE_PATH.open("wb")
        zip_data = requests.get(ZIP_URL, timeout=30).content
        zipfile_obj.write(zip_data)
        zipfile_obj.close()
    else:
        logger.info("Existing zipfile found")
    file_zip_status = zipfile.is_zipfile(ZIPFILE_PATH)
    if not file_zip_status:
        logger.error("%s is not a valid zip archive", ZIPFILE_PATH)
        raise zipfile.BadZipFile()
    logger.info("%s is a zip archive by magic number", ZIPFILE_PATH)
    with zipfile.ZipFile(ZIPFILE_PATH, mode="r") as channels_zipfile:
        first_bad_file = channels_zipfile.testzip()
        if first_bad_file is None:
            logger.info("%s is a valid zip archive", ZIPFILE_PATH)
        else:
            logger.error(
                ("%s is not a valid zip archive,"
                 " the first bad file found was %s"),
                ZIPFILE_PATH,
                first_bad_file)
            raise zipfile.BadZipFile()


if __name__ == "__main__":
    next_nothing_re = re.compile(r"Next nothing is (\d+)", flags=re.IGNORECASE)
    _load_data()
    with zipfile.ZipFile(ZIPFILE_PATH, mode="r") as channels:
        CURRENT_NOTHING = 90052
        comments = list()
        while CURRENT_NOTHING:
            with channels.open(f"{CURRENT_NOTHING}.txt") as current_file:
                current_text = current_file.read().decode("utf-8")
                print(current_text)
                comments.append(channels.getinfo(
                    f"{CURRENT_NOTHING}.txt").comment.decode("utf-8"))
                next_nothing_match = next_nothing_re.search(current_text)
                CURRENT_NOTHING = next_nothing_match.group(
                    1) if next_nothing_match is not None else None
        print(''.join(comments))
