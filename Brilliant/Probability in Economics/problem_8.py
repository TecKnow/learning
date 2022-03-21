from random import random
from statistics import mean


def get_price():
    price = 60
    roll = random()
    if roll <= 0.2:
        price *= 0.9
    else:
        price *= 1.05
    roll = random()
    if roll <= 0.7:
        price *= 0.96
    else:
        price *= 1.08
    return price


print(mean(get_price() for i in range(1000000)))
