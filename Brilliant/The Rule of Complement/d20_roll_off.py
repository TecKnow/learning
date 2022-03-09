import fractions

if __name__ == "__main__":
    alice = range(1, 21)
    bill = range(1, 21)
    permutations = 0
    alice_wins = 0
    for alice_roll in alice:
        for bill_roll in bill:
            permutations += 1
            if alice_roll > bill_roll:
                alice_wins += 1
    win_proportion = fractions.Fraction(alice_wins, permutations)
    print(win_proportion)
