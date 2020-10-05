def format_fixed_width(list_of_lists, padding=2, widths=None, alignments=None):
    padding_width = padding
    # rows = tuple((tuple(x) for x in list_of_lists))
    rows = tuple(tuple(x.lstrip() for x in row) for row in list_of_lists)
    columns = tuple(zip(*rows))
    if alignments is None:
        alignments = ["L"] * len(columns)
    if widths is None:
        max_lengths = tuple(max(len(x) for x in column) for column in columns)
    else:
        max_lengths = widths
    columns_max = tuple(zip(columns, max_lengths, alignments))
    column_word_pairs = tuple(tuple((word, column[1], column[2]) for word in column[0]) for column in columns_max)
    row_word_pairs = tuple(zip(*column_word_pairs))
    res = list()
    for row in row_word_pairs:
        res_row = [(word[0].ljust(word[1]) if word[2] == "L" else word[0].rjust(word[1])) + " " * padding_width for word
                   in
                   row]
        res_row = ''.join(res_row).rstrip()
        res.append(res_row)
    res = '\n'.join(res)
    return res
