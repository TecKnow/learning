def parse_ranges(ranges: str):
    items = ranges.split(',')
    item: str
    for item in items:
        if '->' in item:
            idx = item.find('->')
            item = item[:idx]
            yield int(item)
        elif '-' in item:
            begin, end = item.split('-')
            yield from range(int(begin), int(end) + 1)
        else:
            yield int(item)
