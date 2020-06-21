from collections import UserString
from collections.abc import MutableSequence
from contextlib import contextmanager


class MutableString(MutableSequence, UserString):

    @contextmanager
    def data_list(self):
        data_as_list = list(self.data)
        yield data_as_list
        self.data = ''.join(data_as_list)

    def __setitem__(self, key, value):
        with self.data_list() as data_as_list:
            data_as_list[key] = value

    def __delitem__(self, key):
        with self.data_list() as data_as_list:
            del data_as_list[key]

    def __len__(self):
        return len(self.data)

    def insert(self, index, obj):
        with self.data_list() as data_as_list:
            data_as_list.insert(index, obj)
