#!/usr/bin/env python3
"""
Problem  : Merge Two Sorted Arrays
URL      : http://rosalind.info/problems/mer/
Author   : David P. Perkins
"""

def merge(a,b):
    a, b = list(a), list(b)
    c = list()
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    c.extend(a)
    c.extend(b)
    
    return c
if __name__ == "__main__":
    with open("merIn.txt", "r") as infile, open("merOut.txt", "w") as outfile:
        infile.readline()
        a = [int(x) for x in infile.readline().split()]
        infile.readline()
        b = [int(x) for x in infile.readline().split()]

        print(*merge(a,b), file=outfile)
