if __name__ == "__main__":
    with open("RosTREEin.txt") as infile:
        lines = infile.readlines()
        nodeCount = int(lines[0])
        lines = [(int(x), int(y)) for x, y in [line.split() for line in [x.strip() for x in lines[1:]]]]
        branches = [set((x,)) for x in range(1, nodeCount+1)]
        for x, y in lines:
            preservedBranches = [branch for branch in branches if not x in branch and not y in branch]
            mergedBranches = [branch for branch in branches if x in branch or y in branch]
            branches = preservedBranches + [set.union(*mergedBranches)]
        #print(branches)
        print(len(branches)-1)
