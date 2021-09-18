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

