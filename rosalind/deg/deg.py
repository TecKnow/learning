#!/usr/bin/env python3
"""
Problem  : Insertion Sort
URL      : http://rosalind.info/problems/ins/
Author   : David P. Perkins
"""
nodes = dict()

if __name__ == "__main__":
    with open("degIn.txt", "r") as infile:
        infile.readline()
        for line in infile:
            a, b = [int(x) for x in line.split()]
            nodes.setdefault(a, set()).add(b)
            nodes.setdefault(b, set()).add(a)
        res = [len(nodes[x]) for x in sorted(nodes)]
        print(*res)
