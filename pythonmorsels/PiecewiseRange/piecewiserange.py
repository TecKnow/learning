class PiecewiseRange:

    def __init__(self, ranges: str):
        elements = ranges.split(",")
        elements = [elem.split("-") for elem in elements]
        elements = [[int(x) for x in element] for element in elements]
        self.elements = elements

    def __iter__(self):
        for element in self.elements:
            if len(element) == 1:
                yield element[0]
            else:
                yield from range(element[0], element[1]+1)

    def __len__(self):
        result = 0
        for element in self.elements:
            if len(element) == 1:
                result += 1
            else:
                result += len(range(element[0], element[1]+1))
        return result

    def __getitem__(self, item):
        remaining_index = item
        for element in self.elements:
            if len(element) == 1:
                if remaining_index == 0:
                    return element[0]
                remaining_index -= 1
            elif len(range(element[0], element[1] + 1)) <= remaining_index:
                remaining_index -= len(range(element[0], element[1] + 1))
            else:
                return range(element[0], element[1] + 1)[remaining_index]


if __name__ == "__main__":
    print(PiecewiseRange('1-2, 6-8, 12-14')[5])
