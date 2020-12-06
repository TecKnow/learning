from typing import Iterable, Set


def parse_data(data: str) -> list[set[str]]:
    data = data.split("\n\n")
    data = [group.split() for group in data]
    print(data)
    data = [[set(person) for person in group] for group in data]
    return data


def any_yes_in_group(groups: Iterable[Iterable[Set[str]]]) -> list[set[str]]:
    groups = [set.union(*group) for group in groups]
    return groups

def all_yes_in_group(groups: Iterable[Iterable[Set[str]]]) -> list[set[str]]:
    groups = [set.intersection(*group) for group in groups]
    return groups


if __name__ == "__main__":
    data = open("Day 6 Data.txt").read()
    data = parse_data(data)
    data = all_yes_in_group(data)
    print(sum(len(x) for x in data))
