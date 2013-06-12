def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

import sys

print( " ".join(
    map(str,
        [x+1 for x in list(find_all(sys.stdin.readline().strip(), sys.stdin.readline().strip()))]
        )
    )
)
