"""Python challenge level 16: Let me get this straight

Solution:  romance
"""
import logging
from pathlib import Path
from itertools import batched, chain
import requests
from PIL import Image, GifImagePlugin

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_ALWAYS

URL: str = "http://www.pythonchallenge.com/pc/return/mozart.html"
IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/mozart.gif"
AUTH = ("huge", "file")
INPUT_PATH = Path("/tmp/mozart.gif")
OUTPUT_PATH = Path("/tmp/straight.gif")

NEAR_WHITE = (252, 252, 252)
PURPLE_BAR = (255, 0, 255)


def _get_data():
    if not INPUT_PATH.exists():
        logger.info("Image file not found, fetching")
        r = requests.get(IMAGE_URL, auth=AUTH, timeout=30)
        INPUT_PATH.open('wb').write(r.content)
    else:
        logger.info("Found existing image file")


if __name__ == "__main__":
    _get_data()
    input_img = Image.open(INPUT_PATH)
    pixels = list(input_img.getdata())
    new_pixels: list[tuple[tuple[int, int, int]]] = list()
    for row in batched(pixels, 640):

        if PURPLE_BAR not in row:
            new_pixels.append(row)
        else:
            new_row = row[row.index(PURPLE_BAR):] + row[:row.index(PURPLE_BAR)]
            new_pixels.append(new_row)
    new_img = Image.new(mode="RGB", size=input_img.size)
    new_img.putdata(list(chain.from_iterable(new_pixels)))
    new_img.save(OUTPUT_PATH)
