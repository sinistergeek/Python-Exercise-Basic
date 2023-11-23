import sys

numbers = [0,1,2,3]

sqrs = map(lambda n:n*n,numbers)
print(sqrs)
print(list(sqrs))
print(sys.getsizeof(sqrs))
print()

squares = [n*n for n in numbers]
print(squares)
print(sys.getsizeof(squares))
