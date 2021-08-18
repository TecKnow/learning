import re
from argparse import ArgumentParser

parser = ArgumentParser(description="Search files for a specified string")
parser.add_argument("query", help="The string to search for")
parser.add_argument("filenames", nargs="+", help="The names of the files to be searched")
parser.add_argument("--ignore-case", "-i", help="case fold before searching", action="store_true")
parser.add_argument("--line-number", "-n", help="Show line numbers", action="store_true")
parser.add_argument("--invert-match", "-v", help="Search for non-matching lines", action="store_true")


def grep(query: str, *filenames: str, ignore_case: bool = False, show_line_nums=False, invert_match=False) -> str:
    # print(f"{query=}, {filenames=}, {ignore_case=}")
    query = re.compile(query, flags=re.IGNORECASE if ignore_case is True else 0)
    for filename in filenames:
        with open(filename) as input_file:
            for line_num, line in enumerate(input_file, start=1):
                query_result = query.search(line)
                if query_result and not invert_match or not query_result and invert_match:
                    filename_part = f"{filename + ':' if len(filenames) > 1 else ''}"
                    line_num_part = f"{str(line_num) + ':' if show_line_nums is True else ''}"
                    yield f"{filename_part}{line_num_part}{line.strip()}".strip()


if __name__ == "__main__":
    args = parser.parse_args()
    results = grep(args.query, *args.filenames, ignore_case=args.ignore_case, show_line_nums=args.line_number,
                   invert_match=args.invert_match)
    for matching_line in results:
        print(matching_line)
