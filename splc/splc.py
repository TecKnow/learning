import fasta

def getCodingRegion(DNAString, introns):
    #print("DNA String", DNAString, "introns", introns)
    codingString = list()
    workingString = DNAString
    while workingString:
            for curIntron in introns:
                if workingString.startswith(curIntron):
                    #print("Working String", workingString, "starts with", curIntron)
                    workingString = workingString[len(curIntron):]
                    #print("New Working String", workingString)
                    break
            else:
                codingString.append(workingString[0])
                workingString = workingString[1:]
            #print("Coding string so far", codingString)
    return ''.join(codingString)

def RNAtoProt(RNAString):

    import sys;

    proFile = open('codon_to_amino_acid_table.txt')
    proTab = proFile.read()
    proTab = proTab.split()
    proTab = zip(proTab[::2], proTab[1::2])
    proTab = dict(proTab)

    codons = map(''.join, zip(*[iter(RNAString)]*3))
    res = [proTab[x] for x in codons]
    res = ''.join(res)
    res, y, z = res.partition("Stop")
    return res

if __name__ == "__main__":
    import sys
    FASTAs = fasta.FASTA.fromList(sys.stdin.readline())
    cr = getCodingRegion(FASTAs[0].value, [x.value for x in FASTAs[1:]])
    rna = cr.replace('T','U')
    prot = RNAtoProt(rna)
    print(prot)
    
