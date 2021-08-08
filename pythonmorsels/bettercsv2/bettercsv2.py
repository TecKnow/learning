from collections.abc import Iterator
from csv import reader
from typing import Optional, Iterable


class FancyReader(Iterator):
    def __init__(self, rows: Iterable[str], fieldnames: Optional[Iterable[str]] = None, delimiter: Optional[str] = ','):
        self.row_reader = reader(rows, delimiter=delimiter)
        self._fieldnames = fieldnames
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

    @property
    def row_type(self):
        if self._row_type is None:
            def row_type_init(instance, *args):
                arg_list = list(args)
                for attr in instance.__slots__:
                    setattr(instance, attr, arg_list.pop(0))

            def row_type_iter(instance):
                yield from (getattr(instance, attr_name) for attr_name in instance.__slots__)

            def row_type_repr(instance):
                class_name = instance.__class__.__name__
                attr_str_seq = [f"{a}='{getattr(instance, a)}'" for a in instance.__slots__]
                attr_str = ", ".join(attr_str_seq)
                return f"{class_name}({attr_str})"

            self._row_type = type("Row", (), {"__slots__": self.fieldnames,
                                              "__init__": row_type_init,
                                              "__iter__": row_type_iter,
                                              "__repr__": row_type_repr})
        return self._row_type
