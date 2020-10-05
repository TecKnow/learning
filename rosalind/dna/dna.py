"""
Problem  :  Counting DNA Nucleotides
URL      :  http://rosalind.info/problems/dna/
Author   :  David Perkins
"""

import sys
str = sys.stdin.readline()
for c in 'ACGT':
    print(str.count(c), end=' ')
