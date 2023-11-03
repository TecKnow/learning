import logging
import requests
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/evil.html"
IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/evil1.jpg"
GFX_URL: str = "http://www.pythonchallenge.com/pc/return/evil2.gfx"

TMP_PATH = Path("/tmp")
GFX_PATH = TMP_PATH / "evil2.gfx"

def _get_data():
    if not GFX_PATH.exists():
        logger.info("GFX file not found, attepmting to download")
        with GFX_PATH.open("wb") as GFX_FILE:
            GFX_FILE.write(requests.get(GFX_URL).content)
    else:
        logger.info("Found existing file")

if __name__=="__main__":
    _get_data()
    with GFX_PATH.open("rb") as GFX_FILE:
        GFX_DATA = GFX_FILE.read()
        for i in range(5):
            with (TMP_PATH / f"image{i}.jpg").open("wb") as IMG_FILE:
                IMG_FILE.write(GFX_DATA[i::5])

