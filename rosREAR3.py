import itertools
import sys

def inverse(permutation):
    x, y = zip(*sorted((tuple(reversed(x)) for x in enumerate(permutation))))
    adjustment = min(permutation)
    y = [i + adjustment for i in y]
    return tuple(y)
def composition(theta, ro):
    pi_list = list([0]*len(ro))
    for x in range(len(pi_list)):
        pi_list[x] = theta[ro[x]-min(ro)]
    return tuple(pi_list)
def getBreakpoints(seq):
    return [i for i in range(1, len(seq)) if abs(seq[i] - seq[i-1]) != 1 ]
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
def doReversal(seq, i,j):
    revapplied = tuple(seq[:i]) + tuple(reversed(seq[i:j])) + tuple(seq[j:])
    return revapplied
def findReversals(seq, reversals):
    """ test each decreasing interval to see if it leads to a reversal that
    removes two breakpoints, otherwise, return a reversal that removes only one """
    doubles = list()
    singles = list()
    IntervalStarts = [i for i, j in decreasing]
    for i, j in decreasing:
        endValue = seq[j-1]                     # ending value of decreasing interval
        predIndex = seq.index(endValue-1)       # index of endValue's predecessor
        k = predIndex+1                         # index of value following predecessor
        if (predIndex in IntervalStarts):       # indirectly verifies that predcessor
            continue                            # is at the end of an increasing interval
        if (j > k):
            if (seq[k] + 1 == seq[j]):
                #print("2:")
                doubles.append(k, j)                   # if reversal removes two breakpoints, do it
        else:
            if (seq[j] + 1 == seq[k]):
                print("2:")
                doubles.append(j, k)                   # if reversal removes two breakpoints, do it
    if (j > k):
        j, k = k,j
    #print ("1:")
    singles.append(j, k)                               # otherwise, settle for removing only one
    return doubles, singles

def countReversals(seq):
    workQueue = list()
    triedSet = set()
    solutions = list()
    pseq = tuple([0]) + tuple(seq) + tuple([len(seq) + 1])

def demo1():
    sigma = [int(x) for x in "1 2 3 4 5 6 7 8 9 10".split()]
    #print("sigma", sigma)
    tau = [int(x) for x in "3 1 5 2 7 4 9 6 10 8".split()]
    #print("tau", tau)
    tauInv = inverse(tau)
    #print("tauInv", tauInv)
    composite = composition(tauInv, sigma)
    #print("composite:", composite)
    print(countReversals(composite))
def demo2():
    sigma = [int(x) for x in "3 10 8 2 5 4 7 1 6 9".split()]
    #print("sigma", sigma)
    tau = [int(x) for x in "5 2 3 1 7 4 10 8 6 9".split()]
    #print("tau", tau)
    tauInv = inverse(tau)
    #print("tauInv", tauInv)
    composite = composition(tauInv, sigma)
    #print("composite:", composite)
    print(countReversals(composite))
def demo3():
    sigma = [int(x) for x in "8 6 7 9 4 1 3 10 2 5".split()]
    #print("sigma", sigma)
    tau = [int(x) for x in "8 2 7 6 9 1 5 3 10 4".split()]
    #print("tau", tau)
    tauInv = inverse(tau)
    #print("tauInv", tauInv)
    composite = composition(tauInv, sigma)
    #print("composite:", composite)
    print(countReversals(composite))
def demo4():
    sigma = [int(x) for x in "3 9 10 4 1 8 6 7 5 2".split()]
    #print("sigma", sigma)
    tau = [int(x) for x in "2 9 8 5 1 7 3 4 6 10".split()]
    #print("tau", tau)
    tauInv = inverse(tau)
    #print("tauInv", tauInv)
    composite = composition(tauInv, sigma)
    #print("composite:", composite)
    print(countReversals(composite))
def demo5():
    sigma = [int(x) for x in "1 2 3 4 5 6 7 8 9 10".split()]
    #print("sigma", sigma)
    tau = [int(x) for x in "1 2 3 4 5 6 7 8 9 10".split()]
    #print("tau", tau)
    tauInv = inverse(tau)
    #print("tauInv", tauInv)
    composite = composition(tauInv, sigma)
    #print("composite:", composite)
    print(countReversals(composite))
    

if __name__=="__main__":
   #demo1()
   #demo2()
   demo3()
   demo4()
   #demo5()

