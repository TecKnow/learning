"""Python challenge level 4: follow the chain

Solution:  peak

Solutions to previous levels: http://wiki.pythonchallenge.com/.

IRC: irc.freenode.net #pythonchallenge

urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough.
"""

import re
import requests


URL: str = "http://www.pythonchallenge.com/pc/def/linkedlist.php"


if __name__ == "__main__":
    with requests.Session() as session:
        page_source = session.get(URL).content.decode('utf-8')
        first_nothing_match = re.search(
            r"linkedlist.php\?nothing=(\d+)", page_source)
        first_nothing = first_nothing_match.group(1)
        payload = {"nothing": first_nothing}
        for i in range(400):
            page_source = session.get(
                URL, params=payload).content.decode('utf-8')
            print(page_source)
            next_nothing_match = re.search(
                r"the next nothing is (\d+)", page_source)
            if next_nothing_match:
                next_nothing = next_nothing_match.group(1)
            else:
                next_nothing = int(next_nothing) / 2
            payload['nothing'] = next_nothing
