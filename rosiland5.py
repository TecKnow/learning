import sys;

proFile = open('table.txt')
proTab = proFile.read()
proTab = proTab.split()
proTab = zip(proTab[::2], proTab[1::2])
proTab = dict(proTab)

testString = sys.stdin.readline()
testUnits = map(''.join, zip(*[iter(testString)]*3))
res = [proTab[x] for x in testUnits]
res = ''.join(res)
res, y, z = res.partition("Stop")
print(res)

