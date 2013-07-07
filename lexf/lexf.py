import sys
import itertools

if __name__=="__main__":
    alphabet = sys.stdin.readline()
    length = int(sys.stdin.readline())
    alphaList = alphabet.split()
    itr = itertools.product(alphaList, repeat=length)
    itr = list(itr)
    itr = map(''.join, itr)
    print(*itr, sep='\n')
    
