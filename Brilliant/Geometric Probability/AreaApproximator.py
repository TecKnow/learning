from math import pi

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
                count += 1
            b += iota
        a += iota
        result = count / (pow(resolution, 2))
    print(f"Count is: {count} area is {pow(resolution, 2)}, internal area is {result}")
    choices = [1-pi/4, 1-pi/3, 1-pi/8, pi/2-1]
    variances = [abs(x - result) for x in choices]
    print(variances)
