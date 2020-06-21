from collections.abc import Sequence


class SequenceZip(Sequence):

    def __init__(self, *sequences):
        self._sequences = tuple(sequences)
        print(self._sequences)

    def __getitem__(self, i: int):
        if i < 0:
            i = len(self) + i
        return tuple(c[i] for c in self._sequences)

    def __len__(self) -> int:
        return min(len(c) for c in self._sequences)
