from collections import Counter


def decrement_counter(counter, value):
    counter[value] = counter[value] - 1
    if counter[value] == 0:
        del counter[value]


def stringify_ranges(ranges):
    ranges = sorted(ranges)
    str_list = list()
    for start, end in ranges:
        if start == end:
            str_list.append(str(start))
        else:
            str_list.append(f"{start}-{end}")
    return ','.join(str_list)


def format_ranges(elements):
    res = list()
    c = Counter(elements)
    while c:
        start = sorted(c, reverse=True).pop()
        query_value = start
        while query_value in c:
            decrement_counter(c, query_value)
            last_found_value = query_value
            query_value = query_value + 1
        res.append((start, last_found_value))
    return stringify_ranges(res)
