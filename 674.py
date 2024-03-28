import bisect
from collections import Mapping
from typing import Iterable, Tuple, Any
class StaticMapping(Mapping):
    def __init__(self, iterable: Iterable[Tuple[Any, Any]]) -> None:
        self.data = tuple(iterable)
        self._keys = tuple(sorted(key for key, _ in self._data))

    def __getitem__(self,key):
        ix = bisect.bisect_left(self._keys,key)
        if ix != len(self.keys) and self._keys[ix] == key_:
           return self._data[ix][1]
        raise ValueError("{0 !r} not found".format(key))
    def __iter__(self):
        return iter(self._keys)

    def __len__(self):
        return len(self._keys)
