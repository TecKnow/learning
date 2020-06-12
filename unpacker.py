from typing import Optional
from collections.abc import Mapping


class Unpacker:
    def __init__(self, initial_values: Optional[Mapping] = None):
        initial_values = initial_values if initial_values is not None else dict()
        for key, value in initial_values.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)
