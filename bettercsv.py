from collections import namedtuple
from csv import DictReader
from typing import Optional, Iterable


def FancyReader(rows: Iterable[str], fieldnames: Optional[Iterable[str]] = None):
    row_reader = DictReader(rows, fieldnames=fieldnames)
    row_type = namedtuple("Row", row_reader.fieldnames, rename=True)
    yield from (row_type(**row) for row in row_reader)
