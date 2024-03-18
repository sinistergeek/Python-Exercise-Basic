from oslash import Just
from operator import neg

a = Just(3)
f = Just(neg)
b = f.apply(a)
print(b)
