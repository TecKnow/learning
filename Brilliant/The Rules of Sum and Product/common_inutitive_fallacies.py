if __name__ == "__main__":
    sum_25 = 0
    only_five_six_combinations = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    for e in range(1, 7):
                        combination = [a, b, c, d, e]
                        combination_sum = sum(combination)
                        less_than_five = [x for x in combination if x < 5]
                        if combination_sum >= 25:
                            sum_25 += 1
                        if not less_than_five:
                            only_five_six_combinations += 1
    print(f"{only_five_six_combinations=}, {sum_25=}")
