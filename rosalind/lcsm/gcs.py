def LCSEasy(strings):
    stringList=list()
    LCSPopMatrix(strings[0:2], stringList)
    print(stringList)

def LCS(strings):
    import operator
    matrix = LCSPopMatrix(strings)
    print("Working: Matrix populated")  
    LCSPos = sorted(matrix.items(), key=operator.itemgetter(1), reverse=True)[0]
    LCS = strings[0][(LCSPos[0][0]-(LCSPos[1])):(LCSPos[0][0]-1)]
    return LCS

def LCSPopMatrix(strings, stringList=[]):
   pos = [0] * len(strings)
   matrix = dict()
   checkPos(pos, matrix, strings, stringList)
   advance(pos, strings)
   while not sum(pos) == 0:
       if sum(pos[-3:]) == 0: print(pos)
       checkPos(pos,matrix,strings)
       advance(pos, strings)
       #print("position is:", pos)
   return matrix

def advance(pos, strings):
   for x in range(len(strings)-1, -1, -1):
      pos[x] = pos[x]+1
      if pos[x] >= len(strings[x]):
         pos[x] = 0
      else:
        break
   return pos

def checkPos(pos, matrix, strings, strLst=[]):
    #print("Position is:", pos)
    #print("Strings are:", strings)
    for x in range(len(strings)-2, -1, -1):
        if not strings[x][pos[x]] == strings[x-1][pos[x-1]]:
            break
    else:
        matrix[tuple(pos)] = matrix.get(tuple((x-1 for x in pos)),0) + 1
        print("Trying to insert", strings[0][(pos[0]-(matrix[tuple(pos)])):(pos[0])])
        strLst.append(strings[0][(pos[0]-(matrix[tuple(pos)]-1)):(pos[0]+1)])
if __name__=="__main__":
    with open("RosLCSin.txt") as infile, open("RosLCSout.txt", mode="w") as outfile:
        strings = infile.readlines()
        print("Working:", len(strings), "found with max length", max((len(x) for x in strings)))
        print(LCSEasy(strings))
        print("Done!")
