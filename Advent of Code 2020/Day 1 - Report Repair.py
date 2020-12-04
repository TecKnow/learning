
def find_pairs(data):
    data = set(data)
    pairs = set((x, 2020 - x) for x in data)
    filtered_pairs = set((x, y) for (x, y) in pairs if y in data)
    return filtered_pairs


def product_of_pairs(pairs):
    return (x*y for (x,y) in pairs)

def find_triple(data):
    pairs = set((x, 2020-x) for x in data)
    triples = set((x, v, w) for (x, y) in pairs for v in data for w in data if v+w == y)
    return triples

def product_of_triples(triples):
    return ((x*y*z) for (x,y,z) in triples)


if __name__ == "__main__":
    data = set((int(x) for x in open("Day 1 Data.txt")))
    sum_pairs = find_pairs(data)
    product_pairs = product_of_pairs(sum_pairs)
    print(f"Product of pairs {tuple(product_pairs)}")
    triples = find_triple(data)
    product_triples = product_of_triples(triples)
    print(f"Product of triples {tuple(product_triples)}")
