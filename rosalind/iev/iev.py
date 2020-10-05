def expectedDominantPhenotypeOffspring(populationDistribution):
    totalPop = sum(populationDistribution.values())
    homoDCouples = populationDistribution["AA-AA"] + populationDistribution["AA-Aa"]+ populationDistribution["AA-aa"]
    hetCouples = populationDistribution["Aa-Aa"]
    mixedCouples = populationDistribution["Aa-aa"]
    HhomoRCouples = populationDistribution["aa-aa"]

    domOffspringChance = (1) * (homoDCouples/totalPop) + (3/4) * (hetCouples/totalPop) + (1/2) * (mixedCouples/totalPop)
    expectedDomOffspring = 2 * totalPop * domOffspringChance
    return expectedDomOffspring
if __name__ == "__main__":

    import sys

    populationDistribution = dict()
    populationDistribution["AA-AA"] , populationDistribution["AA-Aa"], populationDistribution["AA-aa"] , populationDistribution["Aa-Aa"] , populationDistribution["Aa-aa"] , populationDistribution["aa-aa"] = sys.stdin.readline().split()
    for key in populationDistribution:
        populationDistribution[key] = int(populationDistribution[key])
    #print(populationDistribution)
    print(expectedDominantPhenotypeOffspring(populationDistribution))
