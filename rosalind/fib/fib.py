"""
Problem  : Rabbits and Recurrence Relations
URL      : http://rosalind.info/problems/fib/
Author   : David P. Perkins
"""
import sys

def fibN(offspring, months):
    if months == 1 or months == 2:
        return 1
    else:
        return fibN(offspring, months - 1) + (fibN(offspring, months - 2) * offspring)
    
if __name__ == "__main__":
    args = sys.stdin.readline().split()
    print(fibN(int(args[1]), int(args[0])))
