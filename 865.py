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

class MyClass:
    def method(self):
        return 'instance method called',self

    @classmethod
    def classmethod(cls):
        return 'class method called',cls

    @staticmethod
    def staticmethod():
        return 'static method called'

class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

Pizza(['cheese','tomatoes'])


class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    @classmethod
    def margherita(cls):
        return cls(['mozzarella','tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella','tomatoes','ham'])


import math 

class Pizza:
    def __init__(self,radius,ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return(f'Pizza({self.raidus!r},'
               f'{self.ingredients!r})')
    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

class Repeater:
    def __init__(self,value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value

def bounded_repeater(value,max_repeats):
    for i in range(max_repeats):
        yield value
