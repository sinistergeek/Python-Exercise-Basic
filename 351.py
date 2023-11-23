def double(n):
    return 2*n

numbers = [1,2,3,4]
name = "Foobar"

double_numbers = [double(n) for n in numbers]
print(double_numbers)

double_chars = [double(n) for n in name]
print(double_chars)
