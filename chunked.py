class chunked:
    _EOL = object()
    _INITIAL_VALUE = object()
    _DEFAULT_FILLVALUE = object()

    def __init__(self, iterable, n, *, fill=_EOL):
        self.it = iter(iterable)
        self.n = n
        self.fill = fill
        self.curvalue = self._INITIAL_VALUE

    def __iter__(self):
        return self

    def __next__(self):
        if self.curvalue is self._INITIAL_VALUE or self.curvalue is self._EOL:
            self.curvalue = next(self.it)
        return self._chunker()

    def _chunker(self):
        for _ in range(self.n):
            yield self.curvalue
            try:
                self.curvalue = next(self.it)
            except StopIteration:
                self.curvalue = self._EOL
                return

if __name__ == "__main__":
    squares = (n ** 2 for n in range(10))
    output = chunked(squares, 4)
    print(*output)