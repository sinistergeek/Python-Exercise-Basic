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
dis.dis(compile("(23,'a','b','c')",'','eval'))

class Car:
        car __init__(self,color,mileage,automatic)
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

car1 = Car('red',3812.4,True)
car2 = Car('blue',40231.0,False)

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point','x y z')(1,2,3)
p2 = (1,2,3)
getsizeof(p1)

from collections import namedtuple
Car = namedtuple('Car','color mileage automatic')
car1 = Car('red',3812.4,True)
print(car1)
print(car1.mileage)


from typing import NamedTuple

class Car(NamedTuple):
    color:str
    mileage:float
    automatic: bool

car1 = Car('red',4323.4,True)
print(car1)
print(car1.mileage)

from typin impo namedTuple

class Car(NamedTuple):
    color: str
    mileage:float
    automatic:bool

car1 = Car('red',mileage=323.4,automatic=True)
print(car1.mileage)

from struct import Struct
MyStruct = Struct('i?f')
data = MyStruct.pack(23,False,42.0)
print(data)

from collections import deque
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
print(q)
print(q.popleft())

class BoundedRepeater:
    def __init__(self,value,max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.maxt_repeats:
            raise StopIteration
        self.count += 1
        return self.value

def bounded_repeater(value,max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

def make_pizza(size, *toppings):
    """ Summerize the piza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
