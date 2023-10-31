import requests
import logging
from pathlib import Path
from PIL import Image
from itertools import batched, chain

TMP = Path("/tmp")
IMAGEFILE_PATH = TMP / "cave.jpg"
ODDS_PATH = TMP / "odds.jpg"
EVENS_PATH = TMP / "evens.jpg"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/5808.html"
IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/cave.jpg"


def _load_data():
    """Ths should download the image file to be worked on

    For reasons unknown, unlike all the other data files this one returns
    401 forbidden when accessed by the requests library.  So instead I had
    to download the image to the target location manually."""
    if not IMAGEFILE_PATH.exists():
        logger.info("image file not found, attepmting to download")
        IMAGEFILE_OBJ = IMAGEFILE_PATH.open("wb")
        IMAGE_DATA = requests.get(IMAGE_URL).content
        IMAGEFILE_OBJ.write(IMAGE_DATA)
        IMAGEFILE_OBJ.close()
    logger.info("Found existing file")


if __name__ == "__main__":
    _load_data()
    im = Image.open(IMAGEFILE_PATH)
    im_width, im_height = im.size
    evens_pixels: list[list[tuple[int, int, int]]] = list()
    odds_pixels: list[list[tuple[int, int, int]]] = list()
    image_pixels = list(batched(list(im.getdata()), im_width))
    evens_pixels = image_pixels[::2]
    odds_pixels = image_pixels[1::2]
    odds_image = Image.new(im.mode, im.size)
    odds_image.putdata(list(chain.from_iterable(odds_pixels)))
    odds_image.save(ODDS_PATH)
    even_image = Image.new(im.mode, im.size)
    even_image.putdata(list(chain.from_iterable(evens_pixels)))
    even_image.save(EVENS_PATH)
