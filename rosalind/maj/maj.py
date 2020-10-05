#!/usr/bin/env python3
"""
Problem  : Majority Element
URL      : http://rosalind.info/problems/maj/
Author   : David P. Perkins
"""
import math
import collections

if __name__ == "__main__":
    with open("majIn.txt", "r") as infile, open("majOut.txt", "w") as outfile:
        res = list()
        infile.readline()
        for line in infile:
            curLst = [int(x) for x in line.split()]
            curCount = collections.Counter(curLst)
            commonElement, commonCount = curCount.most_common(1)[0]
            if commonCount > int(math.floor(len(curLst)/2)):
                res.append(commonElement)
            else:
                res.append(-1)
        print(*res)
        print(*res, file=outfile)
