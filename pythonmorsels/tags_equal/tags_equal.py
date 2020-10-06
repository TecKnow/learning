import shlex


def parse_attrs(tag_dict: dict):
    attr_dict = dict()
    for element in tag_dict["attrs"]:
        element: str
        element_parts = element.split("=", 1)
        key = element_parts[0].strip()
        value = element_parts[1:]
        if not key in attr_dict:
            attr_dict[key] = value
    tag_dict["attrs"] = attr_dict
    return tag_dict


def parse_tag(tag: str):
    tag = tag[1:-1].casefold()
    tag = shlex.split(tag)
    tag_data = dict()
    tag_data["name"] = tag[0].strip()
    tag_data["attrs"] = tag[1:]
    tag_data = parse_attrs(tag_data)
    return tag_data


def tags_equal(tag1: str, tag2: str):
    tag1 = parse_tag(tag1)
    tag2 = parse_tag(tag2)
    return tag1 == tag2
