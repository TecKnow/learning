from random import sample


class RandomLooper:

    def __init__(self, *sequences):
        contents = list()
        for sequence in sequences:
            contents.extend(sequence)
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __iter__(self):
        yield from sample(self.contents, len(self))
