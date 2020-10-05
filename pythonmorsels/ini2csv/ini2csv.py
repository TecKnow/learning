import argparse
import sys
import csv
import configparser
from collections import OrderedDict


def prepare_argument_parser():
    parser = argparse.ArgumentParser(description="Convert from an INI style config file to a CSV")
    parser.add_argument("ini_in", help="The INI type file to be converted", nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument("csv_out", help="The resulting CSV type file", nargs='?',
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.add_argument("-c", "--collapsed", help="Collapse output to one row per section", action="store_true")
    return parser


def read_ini_in(in_file_handle):
    config = configparser.ConfigParser()
    config.read_file(in_file_handle, source=in_file_handle.name)
    in_file_handle.close()
    return config


def write_csv_expanded(config, out_file_handle):
    csv_out = csv.writer(out_file_handle)
    for section_name, section_proxy in config.items():
        for key, value in section_proxy.items():
            csv_out.writerow([section_name, key, value])
    out_file_handle.close()


def getFieldnames(config):
    keys = OrderedDict()
    for section_name, section_proxy in config.items():
        keys.update(section_proxy)
    return keys


def write_csv_collapsed(config, out_file_handle):
    fieldnames = getFieldnames(config)
    fieldnames['header'] = None
    fieldnames.move_to_end('header', last=False)
    fieldnames = tuple(fieldnames.keys())
    csv_out = csv.DictWriter(out_file_handle, fieldnames)
    csv_out.writeheader()
    for section_name, section_proxy in config.items():
        if section_name == "DEFAULT":
            continue;
        row_dict = dict(section_proxy.items())
        row_dict['header'] = section_name
        csv_out.writerow(row_dict)
    out_file_handle.close()


def write_csv(config, out_file_handle, collapsed=False):
    if not collapsed:
        write_csv_expanded(config, out_file_handle)
    else:
        write_csv_collapsed(config, out_file_handle)


if __name__ == "__main__":
    parser = prepare_argument_parser()
    args = parser.parse_args()
    ini_config = read_ini_in(args.ini_in)
    args.ini_in.close()
    write_csv(ini_config, args.csv_out, args.collapsed)
    args.csv_out.close()
