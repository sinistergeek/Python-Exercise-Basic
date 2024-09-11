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

class Car:
    def __init__(self,color,mileage):
        self.color = color 
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r},{self.mileage!r}'
                )

    def __str__(self):
        return f'a {sellf.color} car'

class Car(object):
    def __init__(self,color,mileage):
        self.color = color 
        self.mileage = mileage

    def __repr__(self):
        return '{}({!r},{!r})'.format(self.__class__.__name__,
                                      self.color,self.mileage)
    def __unicode__(self):
        return u'a {self.color} car'.format(self=self)

    def __str__(self):
        return unicode(self).encode('utf-8')


class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name) 


def Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r},{self.y!r})'

a = Point(23,42)
b = copy.copy(a)

class Rectangle:
    def __init__(self,topleft,bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return(f'Rectangle({self.topleft!r}, '
               f'{self.bottomright!r})')

rect = Rectangle(Point(0,1),Point(5,6))
srect = copy.copy(rect)

class Base:
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'
