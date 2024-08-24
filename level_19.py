"""Python challenge level 19: Please!

solution: idiot

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
import tempfile
from pathlib import Path
import email
from os import PathLike
import wave

import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TEMP_DIR = Path(tempfile.gettempdir())
HTML_FILE_PATH = TEMP_DIR / "bin.html"

AUTH: tuple[str, str] = ("huge", "file")
URL: str = "http://www.pythonchallenge.com/pc/hex/bin.html"
AUTH = ("butter", "fly")


def get_html_file() -> str:
    """Return the starting file, downloading if needed"""
    if not HTML_FILE_PATH.exists():
        logging.info("bin.html not found, downloading")
        HTML_FILE_PATH.open('w').write(
            requests.get(URL, auth=AUTH, timeout=30).text)
    else:
        logging.info("Found existing copy of bin.html")
    return HTML_FILE_PATH.open().read()


def get_comment_contents(html_content: str) -> str:
    """extract the comment from the HTML file

    the HTML file has a comment containing an email message, extract that"""
    start_pos = html_content.find("<!--")
    end_pos = html_content.find("-->", start_pos)
    return html_content[start_pos:end_pos].removeprefix("<!--").strip()


def save_audio_from_email(email_string: str, file_location: PathLike) -> bool:
    """extract an audio attachment from an email message string"""
    res = False
    parsed_email = email.message_from_string(email_string)
    for part in parsed_email.walk():
        decoded_payload = None
        if part.get_content_maintype() == "audio":
            decoded_payload = part.get_payload(decode=True)
            res = True
            Path(file_location).open('wb').write(decoded_payload)
    return res


def main_function():
    """Step through solving this problem from scratch"""

    intermediate_file_path = TEMP_DIR / "indian.wav"
    output_file_path = TEMP_DIR / "reversed.wav"
    html_contents = get_html_file()
    html_comment = get_comment_contents(html_contents)
    save_audio_from_email(html_comment, intermediate_file_path)

    with (wave.open(str(intermediate_file_path), 'rb') as initial_wav,
          wave.open(str(output_file_path), 'wb') as reversed_wav):
        initial_wav: wave.Wave_read
        reversed_wav: wave.Wave_write
        reversed_wav.setparams(initial_wav.getparams())
        for _ in range(initial_wav.getnframes()):
            reversed_wav.writeframes(initial_wav.readframes(1)[::-1])


if __name__ == "__main__":
    main_function()
