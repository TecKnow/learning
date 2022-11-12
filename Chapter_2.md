#  Chapter 1: Measuring Uncertainty

## Exercises
1. What is the probability of rolling two six-sided dice and getting a value greater than 7?
2. What is the probability of rolling three six-sided dice and getting a valuegreater than 7?
3.  The yankees are playing the Red Sox.  You're a diehard Sox fan and bet your friend they'll win the game.  You'll pay your friend $30 if the Sox lose and your friend will have to pay you only $5 if the Sox win.  What is the probability you have intuitively assinged to the belief that the Red Sox will win?
## Responses

###  Exercise 1

>  1. What is the probability of rolling two six-sided dice and getting a value greater than 7?

The most straightforward way to do this is to enumerate the set of all possible results, called $\Omega$ and in this case containing all possible rolls of 2d6.  count the ones where the toal is 7 or greater, and determine the proportion.  This is tedious to do by hand but can be calculated with the help of a spreadsheet, or in this case the Python code below.

```Python
from itertools import product
from fractions import Fraction

d6 = range(1, 7)

two_d6_rolls = [((x+y), x, y) for x, y in product(d6, repeat=2)]
two_d6_7up = [ s for s, *_ in two_d6_rolls if s > 7 ]
two_d6_7up_probability = Fraction(len(two_d6_7up), len(two_d6_rolls))

print(f"The probability of rolling > 7 on 2d6 is {two_d6_7up_probability}")
```

The answer is $\frac{5}{12}$


###  Exercise 2

>  2. What is the probability of rolling three six-sided dice and getting a valuegreater than 7?

The most straightforward way to do this is to enumerate the set of all possible results, called $\Omega$ and in this case containing all possible rolls of 3d6.  count the ones where the toal is 7 or greater, and determine the proportion.  This is tedious to do by hand but can be calculated with the help of a spreadsheet, or in this case the Python code below.

```Python
from itertools import product
from fractions import Fraction

d6 = range(1, 7)

three_d6_rolls = [((x+y+z), x, y, z) for x, y, z in product(d6, repeat=3)]
three_d6_7_up = [s for s, *_ in three_d6_rolls if s > 7]
three_d6_7_up_probability = Fraction(len(three_d6_7_up), len(three_d6_rolls))

print(f"The probability of rolling > 7 on 3d6 is {three_d6_7_up_probability}")
```

The answer is $\frac{181}{216}$

###  Exercise 3

> 3.  The yankees are playing the Red Sox.  You're a diehard Sox fan and bet your friend they'll win the game.  You'll pay your friend $30 if the Sox lose and your friend will have to pay you only $5 if the Sox win.  What is the probability you have intuitively assinged to the belief that the Red Sox will win?

Let the following:
1.  $P(w)$: The probability that the Sox win
2.  $P(\neg w)$: The probability that the Sox lose

Then determine the ratio of probabilities:

$$
\frac{P(w)}{P(\neg w)} = \frac{\$30}{\$5} = 6
$$

Next, solve for $P(W)$

$$
P(w) = 6\times P(\neg w)
$$

$$
P(w) = 6 \times (1-P(w))
$$

$$
P(w) = 6 - 6 \times P(w)
$$

$$
P(w) + 6 \times P(w) = 6 \cancel{ - 6 \times P(w)} + \cancel{ 6 \times P(w)}
$$

$$
7 \times P(W) = 6
$$

$$
P(W) = \frac{6}{7} \cong 86\%
$$

