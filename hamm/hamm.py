"""
Problem  :  Counting Point Mutations
URL      :  http://rosalind.info/problems/hamm/
Author   :  David Perkins
"""

import sys

a = sys.stdin.readline()
b = sys.stdin.readline()

res = 0
for x, y in zip(a,b):
    if x != y:
        res += 1
print(res)

##GAGCCTACTAACGGGAT
##CATCGTAATGACGGCCT
