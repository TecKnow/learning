"""
Problem  : Fibonacci Numbers
URL      : http://rosalind.info/problems/fibo/
Author   : David P. Perkins
"""
import sys

def fib(n):
    a = 0
    b = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1;
    else:
        for x in range(1,n):
            c = a + b
            a = b
            b = c
    return b
if __name__ == "__main__":
    print(fib(int(sys.stdin.readline().split()[0])))
