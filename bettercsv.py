from collections import namedtuple
from csv import reader
from typing import Iterable


def FancyReader(rows: Iterable[str], fieldnames: Iterable[str]):
    row_type = namedtuple("Row", fieldnames, rename=True)
    row_reader = reader(rows)
    yield from (row_type(*row) for row in row_reader)