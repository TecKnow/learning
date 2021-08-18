from statistics import mean, median
from time import perf_counter
from typing import Optional


class Timer:
    registry = dict()

    def __new__(cls, name: Optional[str] = None, _parent: Optional["Timer"] = None, *args, **kwargs):
        if name is not None and name in cls.registry:
            return cls.registry[name]
        else:
            new_instance = super().__new__(cls, *args, **kwargs)
            if name is not None:
                cls.registry[name] = new_instance
            return new_instance

    def __init__(self, name: Optional[str] = None, _parent: Optional["Timer"] = None):

        if getattr(self, "_existing", False) is False:
            self._parent = _parent  # type: Optional[Timer]
            self._start = self._parent._start if self._parent is not None else None
            self._finish = None
            self.name = name
            self.runs = list()
            self._named_splits = dict()
            self._split_list = list()
            self._existing = True

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finish = perf_counter()
        if self._start is None:
            print(f"Freaking out with {self._parent}")
        self.runs.append(self._finish - self._start)
        self._start = None

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._split_list[item]
        else:
            return self._named_splits[item]

    def split(self, name=None):
        """Creates a sub-timer.

        I'm pretty sure this would reveal some unexpected behavior if you crate a sub timer with the same name as an
        existing timer because of the class level registry.  Split will return an existing timer from the registry but
        it won't be able to update the parent because the constructor won't re-run.  This could be unexpected, but so
        could having the parent of an existing timer change.  Since the requirements are unclear I'm leaving this in.
        """

        if self._start is None:
            raise RuntimeError("Cannot split because parent timer is not running")
        elif name in self._named_splits:
            return self._named_splits[name]
        else:
            new_split = self.__class__(name=name, _parent=self)
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
