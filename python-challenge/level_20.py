"""Python challenge level 20: go away!

solution: ?
"""

import logging
import tempfile
from pathlib import Path

import requests
from PIL import Image

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/hex/bin.html"
IMAGE_URL = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
AUTH = ("butter", "fly")

TEMP_DIR = Path(tempfile.gettempdir())
IMAGE_FILE_PATH = TEMP_DIR / "unreal.jpg"


def _get_data() -> None:
    """Only download the image file if needed"""
    if not IMAGE_FILE_PATH.exists():
        logger.info("Image file not found, downloading")
        IMAGE_FILE_PATH.open('wb').write(
            requests.get(IMAGE_URL, auth=AUTH, timeout=30).content)


def main_function():
    """Step through solving this problem from scratch"""
    _get_data()
    im = Image.open(str(IMAGE_FILE_PATH))
    print(im.format, im.size, im.mode)
    print(im.getdata())


if __name__ == "__main__":
    main_function()
