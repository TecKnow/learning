from argparse import ArgumentParser

parser = ArgumentParser(description="Search files for a specified string")
parser.add_argument("query", help="The string to search for")
parser.add_argument("filenames", nargs="+", help="The names of the files to be searched")
parser.add_argument("--ignore-case", "-i", help="case fold before searching", action="store_true")


def grep(query: str, *filenames: str, ignore_case: bool = False) -> str:
    # print(f"{query=}, {filenames=}, {ignore_case=}")
    query = query.casefold() if ignore_case else query
    for filename in filenames:
        with open(filename) as input_file:
            for line in input_file:
                working_line = line.casefold() if ignore_case else line
                if query in working_line:
                    yield f"{filename+':' if len(filenames)>1 else ''}{line}".strip()


if __name__ == "__main__":
    args = parser.parse_args()
    results = grep(args.query, *args.filenames, ignore_case=args.ignore_case)
    for matching_line in results:
        print(matching_line)
