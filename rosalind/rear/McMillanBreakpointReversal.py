import random
import sys

def makePermutation(n):
    """ generates a random permuation of the numbers 1..n-1 sandwiched between 0 and n """
    seq = list(range(1,n))
    random.shuffle(seq)
    return [0] + seq + [n]

def hasBreakpoints(seq):
    """ returns True if sequnces in not strictly increasing by 1 """
    for i in range(1, len(seq)):
        if (seq[i] != seq[i-1] + 1):
            return True
    return False

def getStrips(seq):
    """ find contained intervals where sequence is ordered, and return intervals
    in as lists, increasing and decreasing. Single elements are considered
    decreasing. "Contained" excludes the first and last interval. """
    deltas = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    increasing = list()
    decreasing = list()
    start = 0
    for i, diff in enumerate(deltas):
        if (abs(diff) == 1) and (diff == deltas[start]):
            continue
        if (start > 0):
            if deltas[start] == 1:
                increasing.append((start, i+1))
            else:
                decreasing.append((start, i+1))
        start = i+1
    return increasing, decreasing

def pickReversal(seq, decreasing):
    """ test each decreasing interval to see if it leads to a reversal that
    removes two breakpoints, otherwise, return a reversal that removes only one """
    IntervalStarts = [i for i, j in decreasing]
    for i, j in decreasing:
        endValue = seq[j-1]                     # ending value of decreasing interval
        predIndex = seq.index(endValue-1)       # index of endValue's predecessor
        k = predIndex+1                         # index of value following predecessor
        if (predIndex in IntervalStarts):       # indirectly verifies that predcessor
            continue                            # is at the end of an increasing interval
        if (j > k):
            if (seq[k] + 1 == seq[j]):
                print("2:")
                return (k, j)                   # if reversal removes two breakpoints, do it
        else:
            if (seq[j] + 1 == seq[k]):
                print("2:")
                return (j, k)                   # if reversal removes two breakpoints, do it
    if (j > k):
        j, k = k,j
    print ("1:")
    return (j, k)                               # otherwise, settle for removing only one

def doReversal(seq, i,j):
    return seq[:i] + [element for element in reversed(seq[i:j])] + seq[j:]

def improvedBreakpointReversalSort(seq):
    while hasBreakpoints(seq):
        increasing, decreasing = getStrips(seq)
        if len(decreasing) > 0:
            reversal = pickReversal(seq, decreasing)
        else:
            print ("0:")
            reversal = increasing[0]
        print(seq, "reversal", reversal)
        seq = doReversal(seq, *reversal)
    print(seq, "Sorted")
    return

if __name__ == "__main__":
    print ("Python implementation of breakpoint reversal sort on page 135")

    while True:
        inputstr = input('Enter a list, the size of list, or 0 to exit:')
        if (inputstr.find(',') > 0):
            L = [int(v) for v in input.split(',')]
        else:
            n = int(inputstr)
            if (n == 0):
                break
            L = makePermutation(n)
        improvedBreakpointReversalSort(L)
