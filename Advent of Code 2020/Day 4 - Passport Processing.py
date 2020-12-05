import re
from typing import Iterable, Mapping, Sequence, Any


def parse_passports(batch_file_text: str) -> list[dict]:
    data = batch_file_text.split("\n\n")
    data = [entry.split() for entry in data]
    data = [[pairs.split(":") for pairs in passports] for passports in data]
    data = [dict(passport) for passport in data]
    return data


def filter_for_complete_passports(passports: Iterable[Mapping[str, Any]],
                                  required_fields=None) -> Sequence[Mapping[str, Any]]:
    if required_fields is None:
        required_fields = set("byr iyr eyr hgt hcl ecl pid".split())
    return [passport for passport in passports if not required_fields.difference(passport.keys())]


def validate_byr(x: int) -> bool:
    return 1920 <= int(x) <= 2002


def validate_iyr(x: int) -> bool:
    return 2010 <= int(x) <= 2020


def validate_eyr(x: int) -> bool:
    return 2020 <= int(x) <= 2030


def validate_hgt(hgt: str) -> bool:
    re_str = r"(?P<height>\d{2,3})(?P<units>in|cm)"
    m = re.match(re_str, hgt)
    if not m:
        return False
    height = int(m.group("height"))
    units = m.group("units")
    if units == "cm":
        return 150 <= height <= 193
    if units == "in":
        return 59 <= height <= 76
    return False


def validate_hcl(hcl: str) -> bool:
    re_str = r"^#([0-9A-Fa-f]){6}$"
    m = re.match(re_str, hcl)
    return bool(m)


def validate_ecl(ecl: str) -> bool:
    return ecl in set("amb blu brn gry grn hzl oth".split())


def validate_pid(pid: str) -> bool:
    return bool(re.match(r"^\d{9}$", pid))


def validate_passport(passport: dict[str, Any]) -> bool:
    return all((validate_byr(passport["byr"]),
               validate_iyr(passport["iyr"]),
               validate_eyr(passport["eyr"]),
               validate_hgt(passport["hgt"]),
               validate_hcl(passport["hcl"]),
               validate_ecl(passport["ecl"]),
               validate_pid(passport["pid"])
               ))


def filter_for_valid_passports(passports: Iterable[dict[str, Any]]) -> Sequence[dict[str, Any]]:
    return [passport for passport in passports if validate_passport(passport)]


if __name__ == "__main__":
    batch_file = open("Day 4 Data.txt").read()
    passports = parse_passports(batch_file)
    complete_passports = filter_for_complete_passports(passports)
    valid_passports = filter_for_valid_passports(complete_passports)
    print(f"Number of valid passports: {len(valid_passports)}")
