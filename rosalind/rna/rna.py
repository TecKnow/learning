"""
Problem  :  Transcribing DNA into RNA
URL      :  http://rosalind.info/problems/rna/
Author   :  David Perkins
"""
import sys
str = sys.stdin.readline()
res = ''
for c in str:
    if c == 'T':
        res = res +'U'
    else:
        res = res + c
print(res)
