import io
import csv


def condense_csv(data, id_name=None):
    entries = dict()
    properties = list()
    input_reader = csv.reader(data.splitlines())
    if id_name is None:
        id_name = next(input_reader)[0]
    properties.append(id_name)
    for ID, property, value in input_reader:
        if property not in properties:
            properties.append(property)
        entries.setdefault(ID, {id_name: ID})[property] = value
    output = io.StringIO()
    writer = csv.DictWriter(output, properties)
    writer.writeheader()
    writer.writerows(entries.values())
    return output.getvalue()
