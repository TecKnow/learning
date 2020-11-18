from random import randint

def game():
    chips = 1
    while 0 < chips < 4:
        roll = randint(1,6)
        if roll <= 3:
            chips -= 1
        elif roll <=5:
            chips += 1
        elif roll == 6:
            chips +=2
        else:
            print("Well that can't happen")
    if chips <= 0:
        return False
    elif chips >= 4:
        return True
    else:
        return "Somehow a draw"

if __name__ == "__main__":
    wins = sum((game() for x in range(10000000)))
    print(f"Number of games won: {wins}")