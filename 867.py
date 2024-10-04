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
