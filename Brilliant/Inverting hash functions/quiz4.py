from csv import writer

with open('hashout.csv', 'w', newline="") as outfile:
    hashwriter = writer(outfile)
    hashwriter.writerow("n x1 x2 add mult hash".split())
    for n in range(256):
        x1 = n >> 4
        x2 = n % 2 ** 4
        x_add = (x1 + x2) % 2 ** 4
        x_mult = (x1 * x2) % 2 ** 4
        x_hash = (x_add << 4) + x_mult
        hashwriter.writerow([n, x1, x2, x_add, x_mult, x_hash])
