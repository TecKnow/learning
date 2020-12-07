if __name__ == "__main__":
    count = 0
    resolution = 10000
    iota = 1 / resolution
    a = 0
    b = 0
    while a <= 1:
        b = 0
        while b <= 1:
            if (pow(a, 2) + pow(b, 2)) <= (2 * min(a, b)):
                count = count + 1
            b += iota
        a += iota
    print(f"Count is: {count} area is {pow(resolution, 2)}, internal area is {count / (pow(resolution, 2))}")
