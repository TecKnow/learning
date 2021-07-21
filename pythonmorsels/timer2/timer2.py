from statistics import mean, median
from time import perf_counter
from typing import Optional


class Timer:
    def __init__(self, func=None, *, _name: Optional[str] = None, _parent: Optional["Timer"] = None):
        self._parent = None  # type: Optional[Timer]
        self._start = self._parent._start if self._parent is not None else None
        self._finish = None
        self._name = None
        self.runs = list()
        self._func = func
        self._named_splits = dict()
        self._split_list = list()

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finish = perf_counter()
        self.runs.append(self._finish - self._start)
        self._start = None

    def __call__(self, *args, **kwargs):
        with self:
            return self._func(*args, **kwargs)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._split_list[item]
        else:
            return self._named_splits[item]

    def split(self, name=None):
        if self._start is None:
            raise RuntimeError("Cannot split because parent timer is not running")
        elif name in self._named_splits:
            return self._named_splits[name]
        else:
            new_split = self.__class__(_name=name, _parent=self)
            self._split_list.append(new_split)
            if name is not None:
                self._named_splits[name] = new_split
            return new_split

    @property
    def elapsed(self):
        return sum(self.runs)

    @property
    def min(self):
        return min(self.runs)

    @property
    def max(self):
        return max(self.runs)

    @property
    def mean(self):
        return mean(self.runs)

    @property
    def median(self):
        return median(self.runs)
