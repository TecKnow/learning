import locale
import argparse
import sys

parser = argparse.ArgumentParser(description="Convert between text encodings")

parser.add_argument("-o", "--output", help="output file")
parser.add_argument("-f", "--from-code", default=locale.getpreferredencoding(False), help="input encoding")
parser.add_argument("-t", "--to-code", default=locale.getpreferredencoding(False), help="output encoding")
parser.add_argument("-c", action="store_const", const="ignore", default="strict", help="Ignore errors")
parser.add_argument("infile", nargs="?", default="-", help="File name of input data")


def process_args(args: argparse.Namespace) -> argparse.Namespace:
    if args.output is None:
        sys.stdout.reconfigure(encoding=args.to_code)
        args.output = sys.stdout
    else:
        args.output = open(args.output, "w", encoding=args.to_code, errors=args.c)
    if args.infile == "-":
        sys.stdin.reconfigure(encoding=args.from_code, errors=args.c)
        args.infile = sys.stdin
    else:
        args.infile = open(args.infile, 'r', encoding=args.from_code, errors=args.c)

    if args.infile is None or args.infile == "-":
        args.infile = sys.stdin
    return args


if __name__ == "__main__":
    args = parser.parse_args()
    args = process_args(args)
    data = args.infile.read()
    args.output.write(data)
    if args.output is not sys.stdout:
        args.output.close()
    if args.infile is not sys.stdin:
        args.infile.close()
