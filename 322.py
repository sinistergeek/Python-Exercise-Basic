import sys

def double(n):
    print(f"double {n}")
    return 2 * n

numbers = [1,2,4,-1,23,53535,3434]

double_numbers = map(double,numbers)
print(double_numbers)
for num in double_numbers:
    print(num)
    if num > 42:
        break

print()
print(sys.getsizeof(numbers))
print(sys.getsizeof(double_numbers))
