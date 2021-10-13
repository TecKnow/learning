from collections.abc import Sequence


class SequenceZip(Sequence):

    def __init__(self, *sequences):
        self._sequences = tuple(sequences)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return SequenceZip(*(s[:len(self)][i] for s in self._sequences))
        if i < 0:
            i = len(self) + i
        return tuple(c[i] for c in self._sequences)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        elif len(self) != len(other):
            return False
        sequence_pairs = zip(self._sequences, other._sequences)
        return all(s[:len(self)] == o[:len(other)] for s, o in sequence_pairs)

    def __len__(self) -> int:
        return min(len(c) for c in self._sequences)

    def __repr__(self):
        sequence_content = (f"{s!r}" for s in self._sequences)
        sequence_string = ', '.join(sequence_content)
        return f"{self.__class__.__name__}({sequence_string})"

    def __setitem__(self, key, value):
        if not len(value) == len(self._sequences):
            raise TypeError(f"expected a sequence of {len(self)} items")
        if key < 0:
            key = len(self) + key

        if key >= len(self):
            raise IndexError("Index out of range")
        for count, item in enumerate(value):
            self._sequences[count][key] = item

    def __delitem__(self, key):
        if key < 0:
            key = len(self) + key
        for elem in self._sequences:
            del elem[key]

    def append(self, new_items):
        if len(new_items) != len(self._sequences):
            raise TypeError(f"Expected a sequence of {len(self._sequences)} items")
        for contained_seq, extension in zip(self._sequences, new_items):
            contained_seq.append(new_items)

    def insert(self, position, new_item):
        if len(new_item) != len(self._sequences):
            raise TypeError(f"Expected a sequence of {len(self._sequences)} items")
        for contained_seq, new_element in zip(self._sequences, new_item):
            contained_seq.insert(position, new_element)


if __name__ == "__main__":
    x, y, z = [0, 1, 2, 3], [4, 5, 6], [7, 8, 9, 10]
    seq = SequenceZip(x, y, z)
    seq.insert(0, (9, 5, 0))
    print(x)
    print(y)
    print(z)
