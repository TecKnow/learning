"""
Problem  :  Open Reading Frames
URL      :  http://rosalind.info/problems/orf/
Author   :  David P. Perkins
"""
import sys

def NucleotideComplement(char):
    assert len(char) == 1, "NucleotideComplement only handles 1 character at a time"
    if char == 'A': return 'T'
    elif char == 'T': return 'A'
    elif char == 'C': return 'G'
    elif char == 'G': return 'C'

def DNAStringComplement(string):
    return ''.join((NucleotideComplement(x) for x in string))

def DNAStringReverseComplement(string):
    return ''.join(reversed(DNAStringComplement(string)))

def CodonToProtTable():
    proFile = open('codon_to_amino_acid_table.txt')
    proTab = proFile.read()
    proFile.close()
    proTab = proTab.split()
    proTab = zip(proTab[::2], proTab[1::2])
    proTab = dict(proTab)
    return proTab

def CodonToProtTranslate(RNASequence):
    codons = map(''.join, zip(*[iter(RNASequence)]*3))
    res = [CodonToProtTranslateTable[x] for x in codons]
    return res

def ProtCandidates(protSequence):
    #print(''.join(protSequence))
    ret = list()
    startIndex = 0
    while True :
        try:
            startIndex = protSequence.index("M", startIndex)
        except ValueError:
            break
        try:
            stopIndex = protSequence.index("Stop",startIndex)
        except ValueError:
            break
            #stopIndex = len(protSequence)
        #print(startIndex, stopIndex,"".join(protSequence[startIndex:stopIndex]))
        ret.append("".join(protSequence[startIndex:stopIndex]))
        startIndex += 1
    #print(ret)
    return ret

def DNAtoRNA(DNASequence):
    return DNASequence.replace("T", "U")

def orf(DNASequence):
    RNASequence = DNAtoRNA(DNASequence)
    RNAComp = DNAtoRNA(DNAStringReverseComplement(DNASequence))
    ProtSequences = [CodonToProtTranslate(RNASequence),
                     CodonToProtTranslate(RNASequence[1:]),
                     CodonToProtTranslate(RNASequence[2:]),
                     CodonToProtTranslate(RNAComp),
                     CodonToProtTranslate(RNAComp[1:]),
                     CodonToProtTranslate(RNAComp[2:])]
    return "\n".join(sorted({y for x in ProtSequences for y in ProtCandidates(x)}))

CodonToProtTranslateTable = CodonToProtTable()

if __name__ == "__main__":
   print(orf("".join(sys.stdin.readline().strip().splitlines()[1:])))
