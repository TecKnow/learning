with open("infile.txt") as ifile, open("outfile.txt", mode='w') as outfile :
    beginDic = dict()
    endDic = dict()
    name = str()
    DNAStr = str()
    k = 3
    edges = set()
    for line in ifile:
        if line.startswith(">"):
            if len(name) > 0 and len(DNAStr) > 0:
                beginDic.setdefault(DNAStr[:k], set()).add(name)
                endDic.setdefault(DNAStr[-k:], set()).add(name)
            name = line[1:].strip()
            DNAStr = str()
        else:
            DNAStr += line.strip()
    #print("begins: ", beginDic)
    #print("ends: ", endDic)
    for tail in endDic:
        if tail in beginDic:
            tailSet = endDic.get(tail)
            headSet = beginDic.get(tail)
            print("Tail set: ", sorted(tailSet))
            print("Head set: ", sorted(headSet))
            print()
            edges.update({(x, y) for x in tailSet for y in headSet if not x == y})

    for cur in sorted(edges):
        #print(*cur)
        print(*sorted(cur), file = outfile)
