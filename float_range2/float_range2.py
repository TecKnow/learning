from math import ceil
from itertools import islice


class float_range:
    def __init__(self, *args):
        num_args = len(args)
        self._len = 0
        if num_args == 0:
            raise TypeError(f"{self.__class__.__name__} expected 1 arguments, got {num_args} ")
        elif num_args > 3:
            raise TypeError(f"{self.__class__.__name__} expected at most 3 arguments, got {num_args}")
        else:
            self.start = 0 if num_args == 1 else args[0]
            self.stop = args[0] if num_args == 1 else args[1]
            self.step = 1 if num_args < 3 else args[2]
            self._len = max(0, ceil((self.stop - self.start) / self.step))
            self._last_item = self.start + ((len(self) - 1) * self.step)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return [self[idx] for idx in range(*item.indices(len(self)))]
        elif not -1 * len(self) <= item < len(self):
            raise IndexError(f"{self.__class__.__name__} object index out of range")
        item = len(self) + item if item < 0 else item
        return self.start + self.step * item

    def __len__(self):
        return self._len

    def __iter__(self):
        current_position = self.start
        while ceil((self.stop - current_position) / self.step) >= 1:
            yield current_position
            current_position += self.step

    def __reversed__(self):
        return (self._last_item + (x * -1 * self.step) for x in range(len(self)))

    def __eq__(self, other):
        if isinstance(other, (range, float_range)):
            if len(self) == 0 and len(other) == 0:
                return True
            elif isinstance(other, float_range):
                return (self.start, self._last_item, self.step) == (other.start, other._last_item, other.step)
            elif isinstance(other, range):
                return (self.start, self._last_item, self.step) == (other.start, other[-1], other.step)
        else:
            return other.__eq__(self)

    def __repr__(self):
        if self.step == 1:
            return f"float_range({self.start}, {self.stop})"
        else:
            return f"float_range({self.start}, {self.stop}, {self.step}) "
