#!/usr/bin/env python3

import tokenize
from io import StringIO
from textwrap import dedent
from token import STRING, NL
import sys


def concat_check_files_messages(file_names):
    for file_name, line_number in concat_check_files(file_names):
        yield f"{file_name}, line {line_number}: implicit concatenation"


def concat_check_files(file_names):
    yield from ((file_name, line) for file_name in file_names for line in concat_check_file(tokenize.open(file_name)))

# I learned that token.NL is the token for a newline that does not end a statement from the reference solutions for this
# exercise, but I am updating it because I want a record of this information if I ever come back to this.
def concat_check_file(file_handle):
    tokens = tokenize.generate_tokens(file_handle.readline)
    open_string = None
    for token in tokens:
        if open_string is None and token[0] == STRING:
            open_string = token
        elif open_string is not None and token[0] == STRING:
            yield open_string[3][0]
        elif open_string is not None and token[0] != NL:
            open_string = None


if __name__ == "__main__":
    for message in concat_check_files_messages(sys.argv[1:]):
        print(message)

