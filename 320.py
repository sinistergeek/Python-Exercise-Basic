def double(n):
    return 2 * n

numbers = [1,2,3,4]
name = "FooBar"

double_numbers = []

for num in numbers:
    double_numbers.append(double(num))
print(double_numbers)

double_letters = []
for cr in name:
    double_letters.append(double(cr))
print(double_letters)
