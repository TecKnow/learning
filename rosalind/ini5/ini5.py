import sys

with open("RosINI5in.txt") as infile:
    lines = infile.readlines()
    savedLines = lines[1::2]
    savedLines = map(str.strip, savedLines)
    print(*savedLines, sep="\n")
