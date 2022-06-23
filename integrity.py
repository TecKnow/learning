import logging
import requests
import bz2

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/def/integrity.html"
LINK: str = "http://www.pythonchallenge.com/pc/return/good.html"
UN = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
PW = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

if __name__ == "__main__":
    inflated_un = bz2.decompress(UN)
    inflated_pw = bz2.decompress(PW)
    print(inflated_un.decode('utf-8'))
    print(inflated_pw.decode('utf-8'))
