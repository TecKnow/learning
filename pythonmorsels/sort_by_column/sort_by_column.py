import argparse
import csv
import sys

DESC_STRING = """Sort a CSV file by the columns provided."""

parser = argparse.ArgumentParser(description=DESC_STRING)
parser.add_argument("infile", help="CSV file for input")
parser.add_argument("columns", nargs="+", help="The column by which to sort, 0-indexed.")
parser.add_argument("--with-header", help="preserve a header row", action="store_true")


def sort_by_column(infile, columns, header=False):
    with open(infile, newline='') as csv_in:
        col_types = list()
        for column in columns:
            column: str
            if ":" in column:
                col_num, col_type = column.split(':')
                col_num = int(col_num)
            else:
                col_type = "str"
                col_num = int(column)
            col_types.append((col_num, col_type))

        col_types = tuple((int(col_num), float if col_type == "num" else str) for (col_num, col_type) in col_types)

        reader = csv.reader(csv_in)
        if header:
            header_row = next(reader)
        sorted_rows = sorted(reader, key=lambda row: tuple(col_type(row[col_num]) for (col_num, col_type) in col_types))
        writer = csv.writer(sys.stdout)
        if header:
            writer.writerow(header_row)
        writer.writerows(sorted_rows)


if __name__ == "__main__":
    args = parser.parse_args()
    sort_by_column(args.infile, args.columns, args.with_header)
