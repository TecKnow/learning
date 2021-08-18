import collections.abc
from bisect import bisect_left, bisect_right
from collections import UserList


# Informed by the SORTEDCOLLECTION Python recipe at https://code.activestate.com/recipes/577197-sortedcollection/


class SortedList(UserList, collections.abc.Sequence):

    def __init__(self, *args, key=(lambda x: x), reverse=False):
        super().__init__()
        self.data = list(*args)
        self._key = key
        self._reverse = reverse
        self.data.sort(key=self._key, reverse=self._reverse)
        self._keys = [self._key(i) for i in self.data]

    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)

    def __setitem__(self, key, value):
        raise TypeError(f"'{self.__class__.__name__}' object does not support item assignment")

    def append(self, item):
        raise TypeError(f"'{self.__class__.__name__}' object does not support item assignment")

    def insert(self, i, item):
        raise TypeError(f"'{self.__class__.__name__}' object does not support item assignment")

    def add(self, item):
        k = self._key(item)
        i = bisect_right(self._keys, k)
        self._keys.insert(i, k)
        self.data.insert(i, item)

    def index(self, value, start=0, stop=None):
        stop = min(len(self._keys), stop if stop is not None else len(self._keys))
        k = self._key(value)
        i = bisect_left(self._keys, k, start, stop)
        if i < stop and self.data[i] == value:
            return i
        raise ValueError

    def remove(self, item):
        i = self.index(item)
        del self.data[i]
        del self._keys[i]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def find(self, value, start=0, end=None):
        end = min(len(self._keys), end if end is not None else len(self._keys))
        k = self._key(value)
        i = bisect_left(self._keys, k, start, end)
        if i < end and self.data[i] == value:
            return i
        return -1

    def rfind(self, value, start=0, end=None):
        end = min(len(self._keys), end if end is not None else len(self._keys))
        k = self._key(value)
        i = bisect_right(self._keys, k, start, end)
        if i > start and self.data[i - 1] == value:
            return i - 1
        return -1

    def count(self, item) -> int:
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return self.data[i:j].count(item)

    def __contains__(self, item) -> bool:
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return item in self.data[i:j]
