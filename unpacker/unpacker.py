from collections import OrderedDict
from collections.abc import Mapping
from typing import Optional
from itertools import zip_longest


class Unpacker:
    def __init__(self, initial_values: Optional[Mapping] = None):
        initial_values = initial_values if initial_values is not None else OrderedDict()
        super().__setattr__("_attributes", OrderedDict(initial_values))
        self._attributes  # type: OrderedDict

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return tuple(self._attributes[key] for key in item)
        return self._attributes[item]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            value = tuple(value)
            if len(key) != len(value):
                raise ValueError
            pairs = zip(key, value)
            self._attributes.update(pairs)

        self._attributes[key] = value

    def __getattr__(self, item):
        return self._attributes[item]

    def __setattr__(self, key, value):
        self._attributes[key] = value

    def __iter__(self):
        yield from iter(self._attributes.values())

    def __repr__(self):
        item_strings = (f"{key}={value!r}" for key, value in self._attributes.items())
        items_string = ", ".join(item_strings)
        result = f"{self.__class__.__name__}({items_string})"
        return result
