"""
Problem  : Enumerating Oriented Gene Orderings
URL      : http://rosalind.info/problems/sign/
Author   : David P. Perkins
"""
import itertools

def signedPermute(n):
    elements = range(1, abs(n)+1)
    signedPermutations = list()
    for curPerTuple in itertools.permutations(elements):
        curPer = list(map(int, curPerTuple))
        signedPermutations.append(curPer[:])
        #print("appending base permutation:", curPer)
        curPos = 0
        while curPos < len(curPer):
            #The current digit is 0
            if curPer[curPos] > 0:
                #make a new number, add it to the list, and start the cycle over
                curPer[curPos] = curPer[curPos] * -1
                signedPermutations.append(curPer[:])
                #print("appending:", curPer)
                curPos = 0
            #The current digit is a 1
            elif curPer[curPos] < 0:
                #flip it, then check the next digit
                curPer[curPos] = curPer[curPos] * -1
                curPos += 1
    return len(signedPermutations), signedPermutations
if __name__ == "__main__":
    import sys
    permCount, perms = signedPermute(int(sys.stdin.readline()))
    print(permCount)
    for curPerm in perms:
        print(*curPerm)
