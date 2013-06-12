generations = list()
generations.append({"AA-BB":0, "AA-Bb":0, "AA-bb":0,
                        "Aa-BB":0, "Aa-Bb":1, "Aa-bb":0,
                        "aa-BB":0, "aa-Bb":0, "aa-bb":0})
probMatrix = dict()
probMatrix["AA-BB"] = {"AA-BB":((2/4) *(2/4)), "AA-Bb":((2/4) * (2/4)), "AA-bb":((2/4) * (0/4)),
                        "Aa-BB":((2/4) * (2/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (0/4)),
                        "aa-BB":((0/4) * (2/4)), "aa-Bb":((0/4) * (2/4)), "aa-bb":((0/4) * (0/4))}

probMatrix["AA-Bb"] = {"AA-BB":((2/4) *(1/4)), "AA-Bb":((2/4) * (2/4)), "AA-bb":((2/4) * (1/4)),
                        "Aa-BB":((2/4) * (1/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (1/4)),
                        "aa-BB":((0/4) * (1/4)), "aa-Bb":((0/4) * (2/4)), "aa-bb":((0/4) * (1/4))}

probMatrix["AA-bb"] = {"AA-BB":((2/4) *(0/4)), "AA-Bb":((2/4) * (2/4)), "AA-bb":((2/4) * (2/4)),
                        "Aa-BB":((2/4) * (0/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (2/4)),
                        "aa-BB":((0/4) * (0/4)), "aa-Bb":((0/4) * (2/4)), "aa-bb":((0/4) * (2/4))}

probMatrix["Aa-BB"] = {"AA-BB":((1/4) *(2/4)), "AA-Bb":((1/4) * (2/4)), "AA-bb":((1/4) * (0/4)),
                        "Aa-BB":((2/4) * (2/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (0/4)),
                        "aa-BB":((1/4) * (2/4)), "aa-Bb":((1/4) * (2/4)), "aa-bb":((1/4) * (0/4))}

probMatrix["Aa-Bb"] = {"AA-BB":((1/4) *(1/4)), "AA-Bb":((1/4) * (2/4)), "AA-bb":((1/4) * (1/4)),
                        "Aa-BB":((2/4) * (1/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (1/4)),
                        "aa-BB":((1/4) * (1/4)), "aa-Bb":((1/4) * (2/4)), "aa-bb":((1/4) * (1/4))}

probMatrix["Aa-bb"] = {"AA-BB":((1/4) *(0/4)), "AA-Bb":((1/4) * (2/4)), "AA-bb":((1/4) * (2/4)),
                        "Aa-BB":((2/4) * (0/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (2/4)),
                        "aa-BB":((1/4) * (0/4)), "aa-Bb":((1/4) * (2/4)), "aa-bb":((1/4) * (2/4))}

probMatrix["aa-BB"] = {"AA-BB":((0/4) *(2/4)), "AA-Bb":((0/4) * (2/4)), "AA-bb":((0/4) * (0/4)),
                        "Aa-BB":((2/4) * (2/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (0/4)),
                        "aa-BB":((2/4) * (2/4)), "aa-Bb":((2/4) * (2/4)), "aa-bb":((2/4) * (0/4))}

probMatrix["aa-Bb"] = {"AA-BB":((0/4) *(1/4)), "AA-Bb":((0/4) * (2/4)), "AA-bb":((0/4) * (1/4)),
                        "Aa-BB":((2/4) * (1/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (1/4)),
                        "aa-BB":((2/4) * (1/4)), "aa-Bb":((2/4) * (2/4)), "aa-bb":((2/4) * (1/4))}

probMatrix["aa-bb"] = {"AA-BB":((0/4) *(0/4)), "AA-Bb":((0/4) * (2/4)), "AA-bb":((0/4) * (2/4)),
                        "Aa-BB":((2/4) * (0/4)), "Aa-Bb":((2/4) * (2/4)), "Aa-bb":((2/4) * (2/4)),
                        "aa-BB":((2/4) * (0/4)), "aa-Bb":((2/4) * (2/4)), "aa-bb":((2/4) * (2/4))}

def nextGeneration(currentGeneration):
    nextGen = dict()
    for genKey in currentGeneration:
        for genoKey in probMatrix[genKey]:
            nextGen[genoKey] = nextGen.setdefault(genoKey, 0) + 1 *(currentGeneration[genKey] * probMatrix[genKey][genoKey])
    return nextGen

if __name__ == "__main__":

    import sys

##    for x in probMatrix:
##        print(x, sum(probMatrix[x].values()))

    for x in range(100):
        generations.append(nextGeneration(generations[-1]))
    print(generations)
    print(sum(generations[-1].values()))



"""
    "AA-BB":0
    "AA-Bb":0
    "AA-bb":0
    "Aa-BB":0
    "Aa-Bb":0
    "Aa-bb":0
    "aa-BB":0
    "aa-Bb":0
    "aa-bb":0
    """

