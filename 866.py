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

import dis
dis.dis(compile("(23,'a','b','c')",'','eval))

class Car:
        car __init__(self,color,mileage,automatic)
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

car1 = Car('red',3812.4,True)
car2 = Car('blue',40231.0,False)
