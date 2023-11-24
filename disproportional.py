import logging
from string import ascii_lowercase
import xmlrpc.client

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/disproportional.html"
program_URL = "http://www.pythonchallenge.com/pc/phonebook.php"

EVIL_NAME = "Bert"

if __name__=="__main__":
    server_proxy = xmlrpc.client.ServerProxy(program_URL)
    print(server_proxy.phone("Bert"))