def strict_zip(*sequences):
    lengths = {len(s) for s in sequences}
    if len(lengths) > 1:
        raise ValueError()
    else:
        return list(zip(*sequences))
