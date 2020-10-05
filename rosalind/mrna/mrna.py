"""
Problem  : Inferring mRNA from Protein
URL      : http://rosalind.info/problems/mrna/
Author   : David P. Perkins
"""
import sys

def CodonToProtTable():
    proFile = open('codon_to_amino_acid_table.txt')
    proTab = proFile.read()
    proFile.close()
    proTab = proTab.split()
    proTab = zip(proTab[::2], proTab[1::2])
    proTab = dict(proTab)
    return proTab
def ProtFromCodonTable():
    codFile = open('codon_to_amino_acid_table.txt')
    codTab = codFile.read()
    codFile.close()
    codTab = codTab.split()
    codTab = zip(codTab[1::2], codTab[::2])
    protDic = dict()
    for prot, cod in codTab:
        protDic.setdefault( prot, list() ).append(cod)
    return protDic
def countRNAString(prot):
    protDic = ProtFromCodonTable()
    ret = 3
    for c in prot:
        ret = ret * len(protDic[c])
    return ret
if __name__ == "__main__":
    print(countRNAString(sys.stdin.readline().strip()) % 1000000)

