import json
from collections import UserDict
from collections.abc import Mapping


class SimpleDict(UserDict, Mapping):
    def __getattr__(self, item):
        return self[item]


def parse(json_str: str) -> SimpleDict:
    return json.loads(json_str, object_hook=lambda d: SimpleDict(**d))
