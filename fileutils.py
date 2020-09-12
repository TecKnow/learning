
def last_lines(file_name: str):
    with open(file_name) as input_file:
        yield from  reversed(input_file.readlines())