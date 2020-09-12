from collections.abc import Sequence


class SliceView(Sequence):

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
