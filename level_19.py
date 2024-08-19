"""Python challenge level 19: Please!

solution: ?

The html at the starting URL contains a comment that begins as follows:

From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!
"""

import logging
from pathlib import Path
import tempfile


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TEMP_DIR = Path(tempfile.gettempdir())

AUTH: tuple[str, str] = ("huge", "file")
URL: str = "http://www.pythonchallenge.com/pc/hex/bin.html"
AUTH = ("butter", "fly")
