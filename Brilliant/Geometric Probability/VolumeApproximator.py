if __name__ == "__main__":
    precision = 1000
    increment = 1 / precision
    total_area = pow(1000, 3)
    included_area = 0
    for x in range(0, precision + 1):
        for y in range(0, precision + 1):
            for z in range(0, precision + 1):
                if x * increment + y * increment + z * increment <= 1:
                    included_area += 1
    print(result := included_area / total_area)
    choices = [1 / 2, 1 / 3, 1 / 4, 1 / 6]
    variances = [x - result for x in choices]
    print(variances)
