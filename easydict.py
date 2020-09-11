from collections import UserDict
from collections.abc import Mapping


class EasyDict(UserDict):
    def __init__(self, initial_values: Mapping = None, *, normalize: bool = False, **keyword_args):
        self.__dict__["normalize"] = normalize
        self.__dict__["data"] = dict()
        super().__init__()
        initial_values = initial_values if initial_values is not None else dict()
        self.data.update(initial_values)
        self.data.update(keyword_args)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        else:
            return NotImplemented

    def __setattr__(self, key, value):
        if self.__dict__["normalize"] is True:
            key = key.replace("_", " ")
        self.data[key] = value

    def __getattr__(self, item):
        if self.__dict__["normalize"] is True:
            item = item.replace("_", " ")
        if item in self.data:
            return self.data[item]
        else:
            raise AttributeError()

    def get(self, key, default=None):
        return self.data.get(key, default)
