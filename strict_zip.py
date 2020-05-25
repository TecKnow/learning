def strict_zip(*iterables):
    iterables = [list(s) for s in iterables]
    lengths = {len(s) for s in iterables}
    if len(lengths) > 1:
        raise ValueError()
    else:
        return list(zip(*iterables))
