"""Python challenge level 13: call him

Solution: italy

phone that <remote /> evil
"""

import logging
import xmlrpc.client

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/disproportional.html"
PROGRAM_URL = "http://www.pythonchallenge.com/pc/phonebook.php"

EVIL_NAME = "Bert"

if __name__ == "__main__":
    server_proxy = xmlrpc.client.ServerProxy(PROGRAM_URL)
    print(server_proxy.phone("Bert"))
