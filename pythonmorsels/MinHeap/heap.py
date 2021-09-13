from collections import UserList
from collections.abc import Collection
from typing import Iterable
import heapq


class MinHeap(UserList, Collection):
    def __init__(self, initial_contents: Iterable):
        super().__init__(initial_contents)
        heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, item)

    def pop(self):
        return heapq.heappop(self.data)

    def peek(self):
        return self.data[0]
