import re

regexp_str = r"^(?P<min>\d+)-(?P<max>\d+) (?P<target>\w+): (?P<password>\w+)$"
regexp_obj = re.compile(regexp_str)


def line_parser(line: str):
    m = regexp_obj.match(line)
    res = {"target": m.group('target'),
           "min": int(m.group('min')),
           "max": int(m.group("max")),
           "password": m.group("password")}
    return res


def password_requirements_checker_a(target: str, min: int, max: int, password: str):
    return min <= password.count(target) <= max


def password_requirements_checker_b(target: str, min: int, max: int, password: str):
    pos_a = min-1
    pos_b = max-1
    str_a = password[pos_a]
    str_b = password[pos_b]
    return (str_a == target or str_b == target) and str_a != str_b


if __name__ == "__main__":
    data = open("Day 2 Data.txt").readlines()
    items = tuple(line_parser(line) for line in data)
    acceptable_a = tuple(password_requirements_checker_a(**item) for item in items)
    print(f"Acceptable under method a: {sum(acceptable_a)}")
    acceptable_b = tuple(password_requirements_checker_b(**item) for item in items)
    print(f"Acceptable under method b: {sum(acceptable_b)}")



