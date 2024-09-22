from collections import ChainMap
dict1 = {'one':1,'two':2}
dict2 = {'three':3,'four':4}
chain = ChainMap(dict1,dict2)
chain['three']

from types import MappingProxyType
writable = {'one':1,'two':2}
read_only = MappingProxyType(writable)
read_only['one']

import array
arr = array.array('f',(1.0,1.5,2.0,2.5))
print(arr[1])
