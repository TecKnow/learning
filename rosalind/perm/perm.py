import itertools
import math
import sys

obs = int(sys.stdin.readline().strip())
print(math.factorial(obs))
perms = itertools.permutations(range(1, obs+1))
for x in perms:
    print(*x)
