import sys

if __name__ == "__main__":
    inStr = sys.stdin.readline()
    homoD, het, homoR = inStr.split()
    homoD, het, homoR = float(homoD), float(het), float(homoR)
    total = homoD + het + homoR

    probs = dict()
    probs["probDD"] = homoD/total * ((homoD - 1) / (total -1))
    probs["probDH"] = homoD/total * (het/(total-1))
    probs["probDR"] = homoD/total * (homoR/(total-1))
    probs["probHD"] = het/total * (homoD/(total-1))
    probs["probHH"] = het/total * ((het-1)/(total-1))
    probs["probHR"] = het/total * (homoR/(total - 1))
    probs["probRD"] = homoR/total * (homoD/(total-1))
    probs["probRH"] = homoR/total * (het/(total-1))
    probs["probRR"] = homoR/total * ((homoR-1)/(total -1))

    print(probs)
    print(sum(probs.values()))

    agProbs = dict()
    agProbs["domP"] = probs["probDD"] + probs["probDH"] + probs["probDR"] + probs["probHD"] + probs["probRD"]
    agProbs["hetRec"] = probs["probHR"] + probs["probRH"]
    agProbs["hetHet"] = probs["probHH"]
    agProbs["recRec"] = probs["probRR"]

    print(agProbs)
    print(sum(agProbs.values()))
    ofProbs = dict()
    ofProbs["hetRec"] = (2/4) * agProbs["hetRec"]
    ofProbs["hetHet"] = (3/4) * agProbs["hetHet"]
    ofProbs["domP"] = agProbs["domP"]

    print(ofProbs)

    finalProb = sum(ofProbs.values())

    print("Final Probability:", finalProb)
    
