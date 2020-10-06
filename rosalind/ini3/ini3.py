import sys

if __name__=="__main__":
    inLine = sys.stdin.readline().strip()
    slicePoints = sys.stdin.readline().strip().split()
    slicePoints = list(map(int, slicePoints))

    print(inLine[slicePoints[0]:slicePoints[1] + 1],
          inLine[slicePoints[2]:slicePoints[3] + 1])
    
