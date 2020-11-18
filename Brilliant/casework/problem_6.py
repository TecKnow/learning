from random import randint
import fractions

def play():
    score = 0
    while -2 < score < 2:
        point_result = randint(1,5)
        if point_result <= 3:
            score += 1
        else:
            score -=1
    if score <= -2:
        return False
    else:
        return True

if __name__ == "__main__":
    n_games = 10000000
    wins = sum((play() for x in range(n_games)))
    print(fractions.Fraction(wins, n_games))