from collections.abc import Iterable


class SliceView(Iterable):

    def _bound_index(self, index):
        if index < 0:
            index = len(self.collection) + index
        index = min(max(0, index), len(self.collection))
        return index

    def __init__(self, collection, start=None, stop=None, step=1):
        self.collection = collection
        self.step = step
        if step < 0:
            self.start = len(collection) - 1 if start is None else start
            self.stop = 0 if stop is None else stop
        else:
            self.start = 0 if start is None else start
            self.stop = len(collection) if stop is None else stop
        (self.start, self.stop) = (self._bound_index(self.start), self._bound_index(self.stop))

    def __iter__(self):
        current_position = self.start
        while self.step > 0 and current_position < self.stop or self.step < 0 and current_position >= self.stop:
            yield self.collection[current_position]
            current_position += self.step


if __name__ == "__main__":
    numbers = [2, 1, 3, 4, 7, 11, 18]
    view = SliceView(numbers, step=-1)
    print(list(view))
