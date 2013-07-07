import sys;

def motifProb(GCProb):
    x = float(GCProb)
    GorCprob = x/2
    TorAprob = (1 - x)/ 2
    return 2*(GorCprob  ** 2 ) + 2*(TorAprob **2)

if __name__ == "__main__":
    with open("RosEVALin.txt") as ifile, open("RosEVALout.txt", mode="w") as ofile:
        fileElements = ifile.read().split()
        #print(fileElements)
        targLength = int(fileElements[0])
        totalLength = int(fileElements[1])
        GCProbs = fileElements[2:]
        #print(GCProbs)
        del fileElements

        res = list()
        for x in GCProbs:
            singleProb = motifProb(x)
            chances = totalLength - targLength + 1
            res.append (singleProb ** targLength * chances)
        print(*res)
