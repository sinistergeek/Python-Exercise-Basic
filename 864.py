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
