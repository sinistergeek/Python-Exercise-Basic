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
