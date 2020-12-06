def parse_data(data: str) -> list[set[str]]:
    data = data.split("\n\n")
    data = [group.split() for group in data]
    print(data)
    data = [[set(person) for person in group] for group in data]
    data = [set.union(*group) for group in data]
    return data


if __name__ == "__main__":
    data = open("Day 6 Data.txt").read()
    data = parse_data(data)
    print(sum(len(x) for x in data))
