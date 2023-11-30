"""Python challenge level 17: eat?

Solution:  baloons

The inset image for this problem is the image from level 4: follow the chain.

"is it the 26th already? call his father and inform him that "the flowers are
on their way". he'll understand."
"""
import re
import bz2
import urllib.parse
import xmlrpc.client

import requests

URL: str = "http://www.pythonchallenge.com/pc/return/romance.html"
REFERENCED_URL: str = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
FIRST_BUSYNOTHING = 12345
AUTH = ("huge", "file")
PHONEBOOK_URL = "http://www.pythonchallenge.com/pc/phonebook.php"
LEOPOLD_URL = "http://www.pythonchallenge.com/pc/stuff/violin.php"
STORED_COOKIE_WORD = (
    'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5'
    '%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX'
    '%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0'
    '%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
)
DECODED_COOKIE_WORD = (b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00'
                       b'\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06'
                       b'\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"'
                       b'\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x'
                       b'\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd'
                       b'\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t'
                       b'\tC\xae$\x90')
DECOMPRESSED_BZIP_STRING = None


def stage_1() -> str:
    with requests.session() as s:
        s.auth = ("huge", "file")
        s.timeout = 30
        next_busynothing = FIRST_BUSYNOTHING
        cookie_word = ""
        while True:
            r = requests.get(REFERENCED_URL,
                             params={"busynothing": next_busynothing},
                             timeout=30)
            new_cookie = r.headers["Set-Cookie"]
            new_info_match = re.search(r"info=([^;]*);", new_cookie)
            if new_info_match:
                cookie_word += new_info_match.group(1)
            page_source = r.content.decode("utf-8")
            next_nothing_match = re.search(
                r"the next busynothing is (\d+)", page_source)
            if next_nothing_match:
                next_busynothing = next_nothing_match.group(1)
            else:
                break
    return cookie_word


def stage_2(url_encoded_string: str) -> bytes:
    return urllib.parse.unquote_to_bytes(
        url_encoded_string.replace("+", "%20")
    )


def stage_3(bzip_bytes: str) -> str:
    return bz2.decompress(bzip_bytes).decode('utf-8')


def stage_4(name: str = "Leopold") -> str:
    server_proxy = xmlrpc.client.ServerProxy(PHONEBOOK_URL)
    return server_proxy.phone(name)


def stage_5():
    r = requests.get(LEOPOLD_URL, timeout=30, auth=("large", "file"), cookies={
                     "info": "the flowers are on their way"})
    return r.text


if __name__ == "__main__":
    if STORED_COOKIE_WORD is None:
        STORED_COOKIE_WORD = stage_1()
        print(STORED_COOKIE_WORD)
    if DECODED_COOKIE_WORD is None:
        DECODED_COOKIE_WORD = stage_2(STORED_COOKIE_WORD)
        print(DECODED_COOKIE_WORD)
    if DECOMPRESSED_BZIP_STRING is None:
        DECOMPRESSED_BZIP_STRING = stage_3(DECODED_COOKIE_WORD)
        print(DECOMPRESSED_BZIP_STRING)
    print(stage_4())
    print(stage_5())
