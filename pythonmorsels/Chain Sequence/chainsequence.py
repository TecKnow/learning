import collections.abc
import typing


class SliceView(collections.abc.Sequence):

    def __init__(self, collection, start=None, stop=None, step=1, _range=None):
        self.collection = collection
        collection_slice = slice(start, stop, step)
        if _range is None:
            self._range = range(*collection_slice.indices(len(self.collection)))
        else:
            self._range = _range

    def __getitem__(self, item):
        if isinstance(item, slice):
            return __class__(self.collection, _range=self._range[item])
        return self.collection[self._range[item]]

    def __len__(self):
        return len(self._range)


class ChainSequence(collections.abc.Sequence):

    def __init__(self, *sequences):
        self.sequences = list(sequences)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SliceView(self, item.start, item.stop, item.step)
        count = item if item >= 0 else len(self) + item
        if count >= len(self):
            raise IndexError(f"{self.__class__.__name__} index out of range")
        for sequence in self.sequences:
            if count < len(sequence):
                return sequence[count]
            else:
                count = count - len(sequence)

    def __len__(self):
        return sum(len(x) for x in self.sequences)

    def __add__(self, other):
        if isinstance(other, typing.Sequence):
            new_sequences = self.sequences[:]
            new_sequences.append(other)
            return self.__class__(*new_sequences)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, typing.Sequence):
            self.sequences.append(other)
            return self
        return NotImplemented

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join([repr(x) for x in self.sequences])})'
