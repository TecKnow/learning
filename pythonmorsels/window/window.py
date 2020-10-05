from collections import deque
from itertools import islice, chain, repeat


def window(seq, window_size, *, fillvalue=None):
    seq_iter = iter(seq)
    fill_iter = repeat(fillvalue)
    infinite_iter = chain(seq_iter, fill_iter)
    current_window = deque(islice(infinite_iter, window_size), window_size)
    if not current_window:
        return
    yield tuple(current_window)
    for x in seq_iter:
        current_window.append(x)
        yield tuple(current_window)
