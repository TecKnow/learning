#!/usr/bin/env python3
"""
Problem  : Double-Degree Array
URL      : http://rosalind.info/problems/ddeg/
Author   : David P. Perkins
"""

if __name__=="__main__":
    with open("ddegIn.txt", "r") as infile, open("ddegOut.txt", "w") as outfile:
        nodeCount = int(infile.readline().split()[0])
        adjl = {x:set() for x in range(1, nodeCount+1)}
        ddegl = list()
        
        for line in infile:
            a, b = [int(x) for x in line.split()]
            adjl.setdefault(a, set()).add(b)
            adjl.setdefault(b, set()).add(a)
        for node in sorted(adjl):
            ddeg = sum([len(adjl[x]) for x in adjl[node]])
            ddegl.append(ddeg)
        print(*ddegl, file=outfile)
