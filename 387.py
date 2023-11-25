import sys

lst = [n*2 for n in range(1000)]
gen = [n*2 for n in range(1000)]

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
print()

print(type(lst))
print(type(gen))
print()

print(lst[4])
print()

print(gen[4])
