from time import perf_counter


class Timer:
    def __init__(self):
        self.elapsed = 0
        self._start = None
        self._finish = None

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finish = perf_counter()
        self.elapsed += self._finish - self._start
