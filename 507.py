def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
sum = add(1,2,3,4,5)
print(sum)

sum = add(1,2,3,4,5,6,7,8,9,10)
print(sum)


def greet(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

greet(name='Edcorner',greeting='Hello')

