def add(*lists_of_numbers):
    lengths = set(tuple(tuple(len(sublist) for sublist in outer_list) for outer_list in lists_of_numbers))
    if len(lengths) != 1:
        raise ValueError
    return [[sum(p) for p in zip(*sublists)] for sublists in zip(*lists_of_numbers)]
