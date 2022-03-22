seconds = 60 * 60
arrival_window = 10*60
from fractions import Fraction


together = 0
total = 0

for a in range(seconds):
    for b in range(seconds):
        if abs(a-b) <= arrival_window:
            together += 1
        total += 1
result = Fraction(together, total)
choices = [Fraction(11/36), Fraction(16,31), Fraction(13/61), Fraction(13/16)]
print([float(result-x) for x in choices])

print(result)