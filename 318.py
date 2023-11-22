import sys

rng = range(3,9,2)
numbers= list(rng)
print(rng)
print(numbers)

others = list(range(2,11,31))
print(others)

print(sys.getsizeof(rng))
print(sys.getsizeof(numbers))
