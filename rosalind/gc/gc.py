import sys

bestSeq= str()
bestPer = 0
name = str()
DNAStr = str()
with open("infile.txt") as infile:
    for line in infile:
        if line.startswith(">"):
            print(name)
            print(DNAStr)
            if((len(DNAStr) > 0 and (DNAStr.count("G") + DNAStr.count("C"))/ len(DNAStr) > bestPer)):
                bestSeq = name
                bestPer = (DNAStr.count("G") + DNAStr.count("C")) / len(DNAStr)
            name = line[1:]
            DNAStr = str()

            

        else:
            DNAStr += line.strip()
if((len(DNAStr) > 0 and (DNAStr.count("G") + DNAStr.count("C"))/ len(DNAStr) > bestPer)):
    bestSeq = name
    bestPer = (DNAStr.count("G") + DNAStr.count("C")) / len(DNAStr)

print(bestSeq)
print(bestPer * 100)
