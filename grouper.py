from collections import defaultdict, UserDict
from typing import Any, Callable, Iterable, Optional, Mapping


class Grouper(UserDict):
    def __init__(self, initial_values: Optional[Iterable] = None, *, key: Callable, ):
        self.key_function = key
        self.data = defaultdict(list)
        if isinstance(initial_values, Mapping):
            self.data.update(initial_values)
        elif isinstance(initial_values, Iterable):
            for item in initial_values:
                self.data[self.key_function(item)].append(item)

    def update(self, items: Iterable) -> None:
        if isinstance(items, Mapping):
            for key, value in items.items():
                self.data[key].extend(value)
        else:
            for item in items:
                self.data[self.key_function(item)].append(item)

    def add(self, item: Any):
        self.data[self.key_function(item)].append(item)

    def group_for(self, item: Any) -> bool:
        return self.key_function(item)
