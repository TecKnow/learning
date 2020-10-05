from itertools import zip_longest


def strict_zip(*iterables):
    sentinel_value = object()
    series = zip_longest(*iterables, fillvalue=sentinel_value)
    for values in series:
        if sentinel_value in values:
            raise ValueError()
        yield values
