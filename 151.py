from collections import deque

queue = deque([],maxlen=3)
print(len(queue))
print(queue.maxlen)

queue.append("Foo")
queue.append("Bar")
queue.append("Baz")
print(queue)

queue.append("Zorg")
print(queue)
