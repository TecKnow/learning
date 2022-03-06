from itertools import permutations

if __name__ == "__main__":
    ps = permutations(range(1, 5))
    scores = list()
    for permutation in ps:
        highest_value = 0
        score = 0
        for e in permutation:
            if e > highest_value:
                highest_value = e
                score += 1
        scores.append(score)
    print(sum(scores) / len(scores))
