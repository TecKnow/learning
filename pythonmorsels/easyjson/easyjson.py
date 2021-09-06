import json
from collections import UserDict, UserList
from collections.abc import MutableSequence, Mapping


class SimpleDict(UserDict, Mapping):
    def __getattr__(self, item):
        return self[item]

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return SimpleDict({x: self.data[x] for x in item})
        else:
            return self.data[item]


class EllipsisList(UserList, MutableSequence):
    def __getitem__(self, item):
        if item is Ellipsis:
            return EllipsisGetter(self)
        else:
            return self.data[item]


class EllipsisGetter:
    def __init__(self, backing_list):
        self.backing_list = backing_list

    def __getitem__(self, item):
        return EllipsisList([element[item] for element in self.backing_list])

    def __getattr__(self, item):
        return self[item]


def object_parser(pairs):
    ret = SimpleDict(pairs)
    for k, v in ret.items():
        if isinstance(v, list):
            ret[k] = EllipsisList(v)
    return ret


def parse(json_str: str) -> SimpleDict:
    ret = json.loads(json_str, object_pairs_hook=object_parser)
    if isinstance(ret, list):
        ret = EllipsisList(ret)
    return ret
