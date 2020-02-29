from collections import UserList
from itertools import cycle


class CyclicList(UserList):
    def __iter__(self):
        return cycle(super().__iter__())

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start if item.start is not None else 0
            stop = item.stop if item.stop is not None else len(self) if start >= 0 else 0
            step = item.step if item.step is not None else 1
            return [self[x] for x in range(start, stop, step)]
        else:
            return super().__getitem__(item % len(self))

    def __setitem__(self, key, value):
        return super().__setitem__((key % len(self)), value)
