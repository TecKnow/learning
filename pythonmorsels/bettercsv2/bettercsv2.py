import functools
from collections.abc import Iterator
from csv import reader
from dataclasses import astuple, make_dataclass
from typing import Optional, Iterable


def row_factory(field_names: Iterable[str]):
    def __iter__(self):
        yield from astuple(self)

    return make_dataclass("Row", field_names, namespace={"__slots__": field_names,
                                                         "__iter__": __iter__})


class FancyReader(Iterator):
    def __init__(self, rows: Iterable[str], fieldnames: Optional[Iterable[str]] = None, delimiter: Optional[str] = ','):
        self.row_reader = reader(rows, delimiter=delimiter)
        self.fieldnames = fieldnames
        self._row_type = None

    def __next__(self):
        return self.row_type(*next(self.row_reader))

    @property
    def line_num(self):
        return self.row_reader.line_num

    @property
    def fieldnames(self):
        if self._fieldnames is None:
            self._fieldnames = next(self.row_reader)
        return self._fieldnames

    @fieldnames.setter
    def fieldnames(self, fieldnames: Iterable[str]) -> None:
        self._fieldnames = list(fieldnames) if fieldnames is not None else None

    @functools.cached_property
    def row_type(self):
        return row_factory(self.fieldnames)
