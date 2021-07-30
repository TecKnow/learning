from collections import ChainMap
from collections import UserDict
from collections.abc import Mapping
from types import MappingProxyType


class ProxyDict(UserDict, Mapping):
    def __init__(self, *args, ):
        super().__init__()
        self.data_writeable = ChainMap(*reversed(args))
        self.data = MappingProxyType(self.data_writeable)

    @property
    def maps(self):
        return list(reversed(self.data_writeable.maps))

    def __repr__(self):
        return f"ProxyDict({', '.join(repr(x) for x in self.maps)})"
