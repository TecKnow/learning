"""Python challenge level 12: dealing evil

Solution: disproportional
Distractors: "Bert is evil! go back!
"""

import logging
from pathlib import Path

import requests

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/evil.html"
IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/evil1.jpg"
GFX_URL: str = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
BROKEN_IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/evil4.jpg"

TMP_PATH = Path("/tmp")
GFX_PATH = TMP_PATH / "evil2.gfx"


def _get_data():
    if not GFX_PATH.exists():
        logger.info("GFX file not found, attepmting to download")
        with GFX_PATH.open("wb") as gfx_file:
            gfx_file.write(
                requests.get(
                    GFX_URL,
                    auth=("huge", "file"),
                    timeout=30).content)
    else:
        logger.info("Found existing file")


if __name__ == "__main__":
    _get_data()
    with GFX_PATH.open("rb") as GFX_FILE:
        GFX_DATA = GFX_FILE.read()
        for i in range(5):
            with (TMP_PATH / f"image{i}.jpg").open("wb") as IMG_FILE:
                IMG_FILE.write(GFX_DATA[i::5])
    response = requests.get(
        BROKEN_IMAGE_URL,
        auth=("huge", "file"),
        timeout=30)
    print(response.content.decode('utf-8'))
