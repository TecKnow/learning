import os
import re
from argparse import ArgumentParser
from math import log10, ceil

parser = ArgumentParser(description="Search files for a specified string")
parser.add_argument("query", help="The string to search for")
parser.add_argument("filenames", nargs="+", help="The names of the files to be searched")
parser.add_argument("--ignore-case", "-i", help="case fold before searching", action="store_true")
parser.add_argument("--line-number", "-n", help="Show line numbers", action="store_true")
parser.add_argument("--invert-match", "-v", help="Search for non-matching lines", action="store_true")
parser.add_argument("--initial-tab", "-T", help="Left pad line numbers", action="store_true")


def grep(query: str,
         *filenames: str,
         ignore_case: bool = False,
         show_line_nums: bool = False,
         invert_match: bool = False,
         initial_tab: bool = False) -> str:
    query = re.compile(query, flags=re.IGNORECASE if ignore_case is True else 0)
    for filename in filenames:
        file_size = os.stat(filename).st_size if initial_tab else None
        num_columns = ceil(log10(file_size)) if file_size is not None else 0
        with open(filename) as input_file:
            for line_num, line in enumerate(input_file, start=1):
                query_result = query.search(line)
                if query_result and not invert_match or not query_result and invert_match:
                    filename_part = f"{filename + ':' if len(filenames) > 1 else ''}"
                    line_num_str = str(line_num).rjust(num_columns) + ":"
                    line_num_part = f"{line_num_str if show_line_nums is True else ''}"
                    tab_part = "\t" if initial_tab and (filename_part or line_num_part) else ""
                    yield f"{filename_part}{line_num_part}{tab_part}{line.strip()}"


if __name__ == "__main__":
    args = parser.parse_args()
    results = grep(args.query, *args.filenames, ignore_case=args.ignore_case, show_line_nums=args.line_number,
                   invert_match=args.invert_match, initial_tab=args.initial_tab)

    for matching_line in results:
        print(matching_line)
