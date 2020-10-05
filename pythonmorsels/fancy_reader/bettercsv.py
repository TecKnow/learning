from collections import namedtuple
from collections.abc import Iterator
from csv import DictReader
from typing import Optional, Iterable


class FancyReader(Iterator):
    def __init__(self, rows: Iterable[str], fieldnames: Optional[Iterable[str]] = None):
        self.row_reader = DictReader(rows, fieldnames=fieldnames)
        self.row_type = namedtuple("Row", self.row_reader.fieldnames, rename=True)

    def __next__(self):
        return self.row_type(**next(self.row_reader))

    @property
    def line_num(self):
        return self.row_reader.line_num
