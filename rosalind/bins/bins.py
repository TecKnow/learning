#!/usr/bin/env python3
"""
Problem  : Binary Search
URL      : http://rosalind.info/problems/bins/
Author   : David P. Perkins
"""

import sys
import math

def bins(target, array, start, stop):
    idx = int(start + math.floor((stop - start) /2 ))
    cur = array[idx]
    if cur < target and idx != start:
        start = idx
    elif cur > target and idx != stop:
        stop = idx
    elif cur == target:
        #print("bing!", idx)
        return idx + 1
    else:
        #print("bong!")
        return -1
    #print(start, stop)
    return bins(target, array, start, stop)

def bini(target, source):
    return [bins(x, source, 0, len(source)) for x in target]

if __name__ == "__main__":
    with open("binsIN.txt", "r") as infile, open("binsOut.txt", "w") as outfile:

        infile.readline()
        infile.readline()
        
        src = infile.readline().split()
        src = [int(x) for x in src]
        
        trg = infile.readline().split()
        trg = [int(x) for x in trg]

        
        res = bini(trg, src)
        print(*res, file=outfile)
        
    
