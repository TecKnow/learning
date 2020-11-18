from random import randint
from statistics import mean


def play():
    while True:
        a, b = randint(1, 6), randint(1, 6)
        if a == 6 or b == 6:
            return a + b


if __name__ == "__main__":
    n_games = 1000000
    print(mean((play() for x in range(n_games))))
