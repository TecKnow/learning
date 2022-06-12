from collections import Counter
import requests
import re

URL: str = "http://www.pythonchallenge.com/pc/def/ocr.html"

def get_page_source(url: str = URL) -> str:
    with requests.Session() as session:
        return session.get(URL).content.decode('utf-8')

def get_blob(page_source: str) -> list[str]:
    comment_re = re.compile("<!--(.*?)-->", flags=re.DOTALL)
    results = comment_re.findall(page_source)
    return results[1]

def count_characters(data: str) -> Counter:
    frequencies = Counter(data)
    return frequencies



if __name__ == "__main__":
    data = get_page_source(URL)
    blob = get_blob(data)
    frequencies = count_characters(blob)
    print(frequencies.most_common())