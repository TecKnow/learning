from csv import DictReader
from typing import TextIO, Dict, Any


def csv_columns(input_file: TextIO, *, headers=None, missing=None) -> Dict[Any, Any]:
    csv_dict_reader = DictReader(input_file, fieldnames=headers, restval=missing)
    result_dict = dict()
    for row in csv_dict_reader:
        for key, value in row.items():
            result_dict.setdefault(key, list()).append(value)
    return result_dict
