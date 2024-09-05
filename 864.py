def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    if value:
        return value
    else:
        return

def foo3(value):
    if value:
        return value

type(foo1(0))
type(foo2(0))
type(foo3(0))

Class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

my_car = Car('red',37281)
print(my_car)

class Car:
    def __init__(self,color, mileage):
        self.color = color 
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

my_car = Car('red',3721)
print(my_car)

class Car:
    def __init__(self, color, mileage):
        self.color = color 
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

my_car = Car('red',37281)
print(my_car)
'{}'.format(my_car)
