#!/usr/bin/env python3

from pathlib import Path
from hashlib import sha1


def get_file_hash(pathname):
    with open(pathname, 'rb') as file_object:
        return sha1(file_object.read()).hexdigest()


def find_duplicates(file_paths):
    print(file_paths)

    # first, place every file into buckets by size.

    # file_sizes = dict()
    # for file_path in file_paths:
    #     file_size = Path(file_path).stat().st_size
    #     file_sizes.setdefault(file_size, set()).add(file_path)
    #
    # # Files with unique sizes must also be unique, so stop considering them.
    # # Only groups of files with identical sizes may have identical contents.
    # duplicate_file_sizes = {size: file_paths for size, file_paths in file_sizes if len(file_paths) > 1}
    #
    # file_sizes_and_hashes = dict()
    # for size, file_paths in duplicate_file_sizes:
    #     for file_path in file_paths:
    #         file_sizes_and_hashes.setdefault((size, get_file_hash(file_path)), set()).add(file_path)
    # return [path_set
    #         for ((file_size, file_hash), path_set) in file_sizes_and_hashes
    #         if len(path_set) > 1]
