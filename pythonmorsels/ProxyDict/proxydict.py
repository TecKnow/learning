from collections import ChainMap
from collections import UserDict
from collections.abc import Mapping
from types import MappingProxyType


class ProxyDict(UserDict, Mapping):
    def __init__(self, *args, ):
        super().__init__()
        self.data_writeable = ChainMap(*reversed(args))
        self.data = MappingProxyType(self.data_writeable)
        self.maps = list(args)

    def __repr__(self):
        return f"ProxyDict({repr(self.maps)[1:-1]})"

    def __str__(self):
        return repr(self)
