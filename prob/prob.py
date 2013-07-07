with open("RosPROBIn.txt") as ifile, open("RosPROBOut.txt", mode="w") as ofile:
    probs = ifile.read().split()
    probs = [float(x) for x in probs]
    res = list()
    for x in probs:
        GorCprob = x/2
        TorAprob = (1 - x)/ 2
        sameProb = 2*(GorCprob  ** 2 ) + 2*(TorAprob **2)
        res.append(sameProb);
    print(*res, file=ofile)
