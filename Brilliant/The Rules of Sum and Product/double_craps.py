if __name__ == "__main__":
    combinations = 0
    matches = 0
    for a in range(1, 7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    sum_1 = a+b
                    sum_2 = c+d
                    combinations += 1
                    if sum_1 == sum_2:
                        matches += 1
print(f"{matches=}, {combinations=}")