from collections import Counter

from fetch_data import get_data

URL: str = "http://www.pythonchallenge.com/pc/def/ocr.html"


def count_characters(data: str) -> Counter:
    frequencies = Counter(data)
    return frequencies



if __name__ == "__main__":
    data = get_data(URL)
    frequencies = count_characters(data)
    print(frequencies.most_common())