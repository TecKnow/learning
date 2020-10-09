from collections.abc import Sequence


class ChainSequence(Sequence):

    def __init__(self, *sequences):
        self.sequences = list(sequences)

    def __getitem__(self, item):
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
