import logging
from itertools import chain
from pathlib import Path
from typing import Literal

import requests
from PIL import Image

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


URL: str = "http://www.pythonchallenge.com/pc/return/italy.html"
IMAGE_URL = "http://www.pythonchallenge.com/pc/return/wire.png"
IMAGE_AUTH = ("huge", "file")

INPUT_PATH = Path("/tmp/wire.png")
OUTPUT_PATH = Path("/tmp/wire2.png")

type Direction = Literal[-1, 0, 1]


def _load_data():
    if not INPUT_PATH.exists():
        logger.info("Image file not found, downloading")
        INPUT_PATH.open('wb').write(requests.get(
            IMAGE_URL, auth=IMAGE_AUTH, timeout=31).content)
    else:
        logger.debug("Found existing image file")


def turn_right(cur_dx: Direction, cur_dy: Direction) -> Direction:
    direction_dict = {
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
        (0, 1): (1, 0)
    }
    return direction_dict[(cur_dx, cur_dy)]


if __name__ == "__main__":
    _load_data()
    original_image = Image.open(INPUT_PATH)
    pixels = list(original_image.getdata())
    img = [[0] * 100 for _ in range(100)]
    pixels_iter = iter(pixels)
    dx, dy = (1, 0)
    x, y = (0, 0)
    while (next_pixel := next(pixels_iter, None)) is not None:
        logger.debug("setting position %d, %d", x, y)
        img[x][y] = next_pixel
        if (nx := x+dx) < 0 or nx >= 100 or (ny := y+dy) < 0 or ny >= 100 or img[nx][ny] != 0:
            dx, dy = turn_right(dx, dy)
        x += dx
        y += dy
    output_img = Image.new(original_image.mode, (100, 100))
    img_stream = list(chain.from_iterable(img))
    print(img_stream)
    output_img.putdata(img_stream)
    output_img.save(OUTPUT_PATH)
