from types import SimpleNamespace
car1 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)
print(car1)

from collections import Counter
inventory = Counter()
loot = {'sword':1,'bread':3}
inventory.update(loot)
print(inventory)

import heapq
q = []
heapq.heappush(q,(2,'code'))
heapq.heappush(q,(1,'eat'))
heapq.heappush(q,(3,'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

my_items = ['a','b','c']
i=0
while i < len(my_items):
    print(my_items[i])
    i+=1

emails={
        'Bob':'bob@example.com',
        'Alice':'alice@example.com',
        }

for name,email in emails.items():
    print(f'{name} -> {email}')

squares = []
for x in range(10):
    suares.append(x*x)

values = []
for item in collection:
    if condition:
        values.append(expression)

original_lst =lst
lst[:] = [7,8,9]
print(lst)

numbers = [1,2,3]
for n in numbers:
    print(n)

repeater =Repeater('Hello')
for item in repeater:
    print(item)

class Repeater:
    def __init__(self,value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self,source):
        self.source = source
    def __next__(self):
        return self.source.value

repeater =Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)

class Repeater:
    def __init__(self,value):
        self.value =value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value

repeater - Repeater('Hello')
for item in repeater:
    print(item)


numbers = [1,2,3]
for n in numbers:
    print(n)

my_list = [1,2,3]
iterator = iter(my_list)

class BoundedRepeater:
    def __init__(self,value,max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundedRepeater('Hello',3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)
