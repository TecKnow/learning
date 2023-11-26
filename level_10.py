"""Python challenge level 10: What are you looking at?

Solution:  5808

len(a[30])=?

sequence.txt:
a= [1, 11, 21, 1211, 111221,
"""


import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

URL: str = "http://www.pythonchallenge.com/pc/return/bull.html"
SEQUENCE_URL: str = "http://www.pythonchallenge.com/pc/return/sequence.txt"

_look_and_say_terms = ['1', '11']


def look_and_say_generate() -> None:
    previous_term = list(_look_and_say_terms[-1])
    next_term = list()
    count_character = previous_term[0]
    count = 0
    for character in previous_term:
        if character == count_character:
            count += 1
        else:
            next_term.append(count)
            next_term.append(count_character)
            count_character = character
            count = 1
    next_term.append(count)
    next_term.append(count_character)
    _look_and_say_terms.append(''.join((str(i) for i in next_term)))


def look_and_say(term: int) -> str:
    while len(_look_and_say_terms) <= term:
        look_and_say_generate()
    return _look_and_say_terms[term]


if __name__ == "__main__":
    l_s_30 = look_and_say(30)
    l_s_30_len = len(l_s_30)
    print(l_s_30)
    print()
    print(
        f"length of the 30th term of the look and say sequence is: {l_s_30_len}")
