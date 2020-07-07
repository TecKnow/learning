from collections.abc import Iterable


class SliceView(Iterable):

    def __init__(self, collection, start=None, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.collection = collection
        self._slice = slice(start, stop, step)

    def __iter__(self):
        iter_indices = self._slice.indices(len(self.collection))
        iter_range = range(*iter_indices)
        return (self.collection[i] for i in iter_range)

    def __len__(self):
        size_indices = self._slice.indices(len(self.collection))
        size_range = range(*size_indices)
        return len(size_range)


if __name__ == "__main__":
    numbers = [2, 1, 3, 4, 7, 11, 18]
    view = SliceView(numbers, step=-1)
    print(list(view))
