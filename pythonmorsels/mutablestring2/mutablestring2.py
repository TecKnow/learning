from collections import UserString
from collections.abc import MutableSequence
from contextlib import contextmanager


class MutableString(MutableSequence, UserString, str):

    @contextmanager
    def data_list(self):
        data_as_list = list(self.data)
        yield data_as_list
        # data_as_list = [str(x) for x in data_as_list]
        self.data = ''.join(data_as_list)

    def __getitem__(self, item):
        return self.__class__(self.data[item])

    def __setitem__(self, key, value):
        with self.data_list() as data_as_list:
            data_as_list[key] = str(value)
        return self

    def __delitem__(self, key):
        with self.data_list() as data_as_list:
            del data_as_list[key]
        return self

    def __len__(self):
        return len(self.data)

    def insert(self, index, obj):
        with self.data_list() as data_as_list:
            data_as_list.insert(index, str(obj))
        return self

    def __imul__(self, other):
        self.data = self.data * other
        return self

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return str(self) != str(other)

    def __str__(self):
        return self.data
