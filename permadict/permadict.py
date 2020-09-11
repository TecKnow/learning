from collections import UserDict


class PermaDict(UserDict):
    def __init__(self, *args, silent=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.silent = silent

    def __setitem__(self, key, value):
        if key in self.data:
            if not self.silent:
                raise KeyError(f"'{key} already in dictionary")
            else:
                return None
        return self.data.__setitem__(key, value)

    def force_set(self, key, value):
        return self.data.__setitem__(key, value)

    def update(self, __m=None, *, force=False, **kwargs):
        if __m is None:
            __m = dict()
        if force:
            return self.data.update(__m, **kwargs)
        return super().update(__m, **kwargs)
