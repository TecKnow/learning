"""
Problem  : Partial Permutations
URL      : http://rosalind.info/problems/pper/
Author   : David P. Perkins
"""
import sys
import math

if __name__ == "__main__":
    inline = sys.stdin.readline().strip().split()
    n = int(inline[0])
    k = int(inline[1])

    perms = math.factorial(n)/math.factorial(n-k)
    print(perms % 1000000)
