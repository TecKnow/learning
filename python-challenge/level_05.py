"""Python challenge level 5: peak hell

Solution: channel

peak hell sounds familiar ?
"""

import pickle
import re

import requests

URL: str = "http://www.pythonchallenge.com/pc/def/peak.html"


if __name__ == "__main__":
    with requests.Session() as session:
        page_source = session.get(URL).content.decode('utf-8')
        pkl_filename = re.search(
            r'<peakhell src="([^"]*)"', page_source).group(1)
        pkl_file = session.get(
            "http://www.pythonchallenge.com/pc/def/" + pkl_filename).content
        unpickled_structure = pickle.loads(pkl_file)
        for row in unpickled_structure:
            for c, v in row:
                print(c * v, sep='', end='')
            print()
