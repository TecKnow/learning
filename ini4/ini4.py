import sys

if __name__=="__main__":
    a, b = sys.stdin.readline().strip().split()
    a, b = int(a), int(b)
    if a % 2 == 0: a += 1
    print(sum(range(a, b+1, 2)))
