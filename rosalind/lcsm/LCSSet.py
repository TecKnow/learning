def CommonSubstrings(S1, S2):
    commonSet = set()
    M = [[0]*(1+len(S2)) for i in range(1+len(S1))]
    longest, x_longest = 0, 0
    for x in range(1,1+len(S1)):
        for y in range(1,1+len(S2)):
            if S1[x-1] == S2[y-1]:
                M[x][y] = M[x-1][y-1] + 1
                #Set addition goes here
                commonSet.add(S1[x-M[x][y]:x])
            else:
                M[x][y] = 0
    #print(commonSet)
    return commonSet
def GeneralCommonSubstrings(strings):
    commonSet = CommonSubstrings(strings[0],strings[1])
    for curStr in strings:
        commonSet = {curCom for curCom in commonSet if curCom in curStr}
        print(len(commonSet))
    return commonSet

if __name__ == "__main__":
    with open("RosLCSin.txt") as infile, open("RosLCSout.txt", mode="w") as outfile:
        strings = infile.readlines()
        strings = [x.strip() for x in strings]
        commonSet = GeneralCommonSubstrings(strings)
        longestCommonSubstring = sorted(commonSet, key=len, reverse=True)[0]
        print(longestCommonSubstring)
        #print(commonSet)
        
        
