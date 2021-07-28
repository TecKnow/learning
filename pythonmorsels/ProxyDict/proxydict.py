from collections import UserDict
from collections import ChainMap
from types import MappingProxyType
from collections.abc import Mapping


class ProxyDict(UserDict, Mapping):
    def __init__(self, *args, **kwargs):
        self.data_writeable = ChainMap(*args, **kwargs)
        self.data = MappingProxyType(self.data_writeable)
        self.maps = self.data_writeable.maps


