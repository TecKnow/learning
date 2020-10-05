"""
Problem  : Mortal Fibonacci Rabbits
URL      : http://rosalind.info/problems/fib/
Author   : David P. Perkins
"""
import sys

def fibD(query, lifespan, offspring = 1):
    if query == 1:
        return [1] + [0] * (lifespan - 1)
    elif query == 2 :
        return [0] + [1] + [0] * (lifespan - 2)
    else:
        prev = fibD(query - 1, lifespan, offspring);
        babies = sum(prev[1:])
        ret = [babies] + prev[:-1]
        print("query:", query, "array", ret)
        return ret;
        
if __name__ == "__main__":
    args = sys.stdin.readline().split()
    print(sum(fibD(int(args[0]), int(args[1]))))
