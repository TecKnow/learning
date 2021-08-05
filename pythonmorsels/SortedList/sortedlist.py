import collections.abc
from collections import UserList
import bisect


class SortedList(UserList, collections.abc.Sequence):

    def __init__(self, *args, key=None, reverse=False, ):
        self.data = list(*args)
        self._key = key
        self._reverse = reverse
        self.data.sort(key=self._key, reverse=self._reverse)

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
        self.data.append(item)
        self.data.sort(key=self._key, reverse=self._reverse)

    def index(self, value, start=0, stop=9223372036854775807):
        return self.data.index(value, start, stop)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def find(self, value, start=0, end=9223372036854775807):
        try:
            return self.data.index(value, start, end)
        except ValueError:
            return -1

    def rfind(self, value, start=0, end=9223372036854775807):
        try:
            trimmed_list = self.data[start:end]
            trimmed_list.reverse()
            segment_index = trimmed_list.index(value)
            index = len(trimmed_list)- 1 - segment_index + start
            return index


        except ValueError:
            return -1