from time import perf_counter


class Timer:
    def __init__(self):
        self._start = None
        self._finish = None
        self.runs = list()

    @property
    def elapsed(self):
        return sum(self.runs)

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finish = perf_counter()
        self.runs.append(self._finish - self._start)
