"""Python challenge level 17: eat?

Solution:  ?

The inset image for this problem is the image from level 4: follow the chain.
"""
import requests

URL: str = "http://www.pythonchallenge.com/pc/return/romance.html"
REFERENCED_URL: str = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
AUTH = ("huge", "file")

if __name__ == "__main__":
    r = requests.get(REFERENCED_URL, auth=AUTH, timeout=30)
    print(r.headers["set-cookie"])