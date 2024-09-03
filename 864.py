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

