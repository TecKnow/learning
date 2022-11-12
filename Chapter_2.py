from itertools import product
from fractions import Fraction

d6 = range(1, 7)

two_d6_rolls = [((x+y), x, y) for x, y in product(d6, repeat=2)]
two_d6_7up = [ s for s, *_ in two_d6_rolls if s >= 7 ]
two_d6_7up_probability = Fraction(len(two_d6_7up), len(two_d6_rolls))

print(f"The probability of rolling >= 7 on 2d6 is {two_d6_7up_probability}")

three_d6_rolls = [((x+y+z), x, y, z) for x, y, z in product(d6, repeat=3)]
three_d6_7_up = [s for s, *_ in three_d6_rolls if s >= 7]
three_d6_7_up_probability = Fraction(len(three_d6_7_up), len(three_d6_rolls))

print(f"The probability of rolling >= 7 on 3d6 is {three_d6_7_up_probability}")