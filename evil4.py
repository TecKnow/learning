import logging
import requests
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

AUTH = ("huge", "file")

URL: str = "http://www.pythonchallenge.com/pc/return/evil.html"
IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/evil1.jpg"
BROKEN_IMAGE_URL: str = "http://www.pythonchallenge.com/pc/return/evil4.jpg"

if __name__=="__main__":
    response = requests.get(BROKEN_IMAGE_URL, auth=AUTH)
    print(response.text)