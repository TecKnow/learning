def interleave(*args):
    iterators = [iter(x) for x in args]
    while iterators:
        for count, cur_iter in enumerate(iterators):
            try:
                yield next(cur_iter)
            except StopIteration as ex:
                iterators[count] = None
        iterators = [x for x in iterators if x is not None]
