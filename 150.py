from collections import deque

items = deque(['foo','bar'])

print(type(items))
print(items)

items.append('zorg')
print(items)
print(len(items))

items.append('zorg')
print(items)

nxt = items.popleft()
print(nxt)
print(items)

print(len(items))

if items:
    print("The queue has items")
else:
    print("The queue is empty")
