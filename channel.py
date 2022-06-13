import requests
from pathlib import Path
import logging
import zipfile
import re

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/def/channel.html"
ZIP_URL = "http://www.pythonchallenge.com/pc/def/channel.zip"

TMP = Path("/tmp")
ZIPFILE_PATH = TMP / "channel.zip"


def _load_data():
    if not ZIPFILE_PATH.exists():
        logger.info("Zipfile not found, attempting to download")
        ZIPFILE_OBJ = ZIPFILE_PATH.open("wb")
        ZIPDATA = requests.get(ZIP_URL).content
        ZIPFILE_OBJ.write(ZIPDATA)
        ZIPFILE_OBJ.close()
    else:
        logger.info("Existing zipfile found")
    file_zip_status = zipfile.is_zipfile(ZIPFILE_PATH)
    if not file_zip_status:
        logger.error(f"{ZIPFILE_PATH} is not a valid zip archive")
        raise zipfile.BadZipFile()
    logger.info(f"{ZIPFILE_PATH} is a zip archive by magic number")
    with zipfile.ZipFile(ZIPFILE_PATH, mode="r") as channels_zipfile:
        first_bad_file = channels_zipfile.testzip()
        if first_bad_file is None:
            logger.info(f"{ZIPFILE_PATH} is a valid zip archive")
        else:
            logger.error(f"{ZIPFILE_PATH} is not a valid zip archive, the first bad file found was {first_bad_file}")
            raise zipfile.BadZipFile()

if __name__ == "__main__":
    next_nothing_re = re.compile(r"Next nothing is (\d+)", flags=re.IGNORECASE)
    _load_data()
    with zipfile.ZipFile(ZIPFILE_PATH, mode="r") as channels:
        current_nothing = 90052
        comments = list()
        while current_nothing:
            with channels.open(f"{current_nothing}.txt") as current_file:
                current_text = current_file.read().decode("utf-8")
                print(current_text)
                comments.append(channels.getinfo(f"{current_nothing}.txt").comment.decode("utf-8"))
                next_nothing_match = next_nothing_re.search(current_text)
                current_nothing = next_nothing_match.group(1) if next_nothing_match is not None else None
        print(''.join(comments))