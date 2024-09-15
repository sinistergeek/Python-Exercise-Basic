Car = namedtuple('Car', 'color mileage')

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red',1234)
c.hexcolor()

class Dog:
    num_legs = 4
    def __init__(self,name):
        self.name = name

jack = Dog('Jack')
jill = Dog('Jill')

class CountedObject:
    num_instances = 0
    
    def __init__(self):
        self.__class__.num_instances += 1

CountedObject.num_instances
