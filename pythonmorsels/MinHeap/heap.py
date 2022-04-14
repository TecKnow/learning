from abc import ABC, abstractmethod
from collections.abc import Collection
from typing import Iterable, Iterator, NamedTuple, Any
import heapq
from functools import total_ordering


class _HeapDataItem(NamedTuple):
    key: Any
    item: Any


@total_ordering
class _ReverseCompare:
    def __init__(self, item):
        self.item = item

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return self.item == other
        else:
            return self.item == other.item

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return self.item >= other
        else:
            return self.item >= other.item


class HeapCollection(Collection, ABC):
    @abstractmethod
    def __init__(self, key=lambda x: x):
        self._key = key

    @abstractmethod
    def push(self, item):
        pass

    def pop(self):
        return heapq.heappop(self.data).item

    def peek(self):
        return self.data[0].item

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator:
        return (x.item for x in self.data)

    def __contains__(self, __x: object) -> bool:
        return __x in (x.item for x in self.data)


class MinHeap(HeapCollection):
    def __init__(self, initial_contents: Iterable, key=lambda x: x):
        super().__init__(key)
        self.data = [_HeapDataItem(self._key(x), x) for x in initial_contents]
        heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, _HeapDataItem(self._key(item), item))


class MaxHeap(HeapCollection):
    def __init__(self, initial_contents: Iterable, key=lambda x: x):
        super().__init__(key)
        self.data = [_HeapDataItem(_ReverseCompare(self._key(x)), x) for x in initial_contents]
        heapq.heapify(self.data)

    def push(self, item):
        reverse_compare_object = _ReverseCompare(self._key(item))
        data_item = _HeapDataItem(reverse_compare_object, item)
        heapq.heappush(self.data, data_item)
