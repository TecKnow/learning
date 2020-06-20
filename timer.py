from statistics import mean, median
from time import perf_counter


class Timer:
    def __init__(self, func=None):
        self._start = None
        self._finish = None
        self.runs = list()
        self._func = func

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finish = perf_counter()
        self.runs.append(self._finish - self._start)

    def __call__(self, *args, **kwargs):
        with self:
            return self._func(*args, **kwargs)

    @property
    def elapsed(self):
        return sum(self.runs)

    @property
    def min(self):
        return min(self.runs)

    @property
    def max(self):
        return max(self.runs)

    @property
    def mean(self):
        return mean(self.runs)

    @property
    def median(self):
        return median(self.runs)
