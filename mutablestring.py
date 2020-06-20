from collections import UserString
from collections.abc import MutableSequence


class MutableString(MutableSequence, UserString):

    def __getitem__(self, item):
        return MutableString(self.data[item])

    def __setitem__(self, key, value):
        data_as_list = list(self.data)
        data_as_list[key] = value
        self.data = ''.join(data_as_list)

    def __delitem__(self, key):
        data_as_list = list(self.data)
        del data_as_list[key]
        self.data = ''.join(data_as_list)

    def __len__(self):
        return len(self.data)

    def insert(self, index, obj):
        data_as_list = list(self.data)
        data_as_list.insert(index, obj)
        self.data = ''.join(data_as_list)
