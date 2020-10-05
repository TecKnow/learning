"""
Problem  : Calculating Protein Mass
URL      : http://rosalind.info/problems/prtm/
Author   : David P. Perkins
"""
monoIsoMassTable =  """
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
"""

monoIsoMassWords = monoIsoMassTable.strip().split()
protMassDict = dict(zip(monoIsoMassWords[::2], map(float, monoIsoMassWords[1::2])))
del(monoIsoMassWords)

def protMass(protString):
    sum = 0
    for prot in protString:
        sum += protMassDict[prot]
    return sum

if __name__ == "__main__":
    import sys
    print(protMass(sys.stdin.readline().strip()))
    
