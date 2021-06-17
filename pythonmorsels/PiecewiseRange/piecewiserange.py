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


if __name__ == "__main__":
    p = PiecewiseRange('1-2, 4, 8-10, 11')
    pl = list(p)
    print(pl)
