"""Python challenge level 11: odd even

Solution: evil
"""

import logging
from pathlib import Path

import requests
from PIL import Image

TMP = Path("/tmp")
IMAGEFILE_PATH = TMP / "cave.jpg"
ODDS_PATH = TMP / "odds.jpg"
EVENS_PATH = TMP / "evens.jpg"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/5808.html"
IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/cave.jpg"


def _load_data():
    if not IMAGEFILE_PATH.exists():
        logger.info("image file not found, attepmting to download")
        imagefile_obj = IMAGEFILE_PATH.open("wb")
        image_data = requests.get(
            IMAGE_URL, auth=("huge", "file"),
            timeout=30).content
        imagefile_obj.write(image_data)
        imagefile_obj.close()
    logger.info("Found existing file")


if __name__ == "__main__":
    _load_data()
    im = Image.open(IMAGEFILE_PATH)
    im_width, im_height = im.size
    image_pixels = list(im.getdata())
    evens_pixels: list[tuple[int, int, int]] = list()
    odds_pixels: list[tuple[int, int, int]] = list()

    evens_pixels = image_pixels[::2]
    odds_pixels = image_pixels[1::2]
    odds_image = Image.new(im.mode, im.size)
    odds_image.putdata(odds_pixels)
    odds_image.save(ODDS_PATH)
    even_image = Image.new(im.mode, im.size)
    even_image.putdata(evens_pixels)
    even_image.save(EVENS_PATH)
