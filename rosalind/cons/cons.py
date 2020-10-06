import sys
DNAStrings = sys.stdin.readline().strip()
DNAStringList = DNAStrings.split('\n')
DNAPos = zip(*DNAStringList)

aList = ["A:"]
cList = ["C:"]
gList = ["G:"]
tList = ["T:"]
Consensus = []

for x in DNAPos:
    consensusCount = 0
    Consensus.append('')
    aList.append(x.count("A"))
    if aList[-1] > consensusCount:
       consensusCount = aList[-1]
       Consensus[-1] = "A"

    cList.append(x.count("C"))
    if cList[-1] > consensusCount:
       consensusCount = cList[-1]
       Consensus[-1] = "C"

    gList.append(x.count("G"))
    if gList[-1] > consensusCount:
       consensusCount = gList[-1]
       Consensus[-1] = "G"

    tList.append(x.count("T"))
    if tList[-1] > consensusCount:
       consensusCount = tList[-1]
       Consensus[-1] = "T"

print(*Consensus, sep='')
print(*aList)
print(*cList)
print(*gList)
print(*tList)
