import logging
from string import ascii_lowercase

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/disproportional.html"

phonewords_transtable = str.maketrans(ascii_lowercase, "22233344455566677778889999")

if __name__=="__main__":
    print("disproportional".translate(phonewords_transtable))