tree = [[]]

def addString(newString):
    activePoint = {"activeNode":tree[0], "activeEdge":"", "activeLength":0}
    for char in newString:
        
