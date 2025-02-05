def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper 

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def trace(func):
    def wrapper(*args,**kwargs):
        print(f'TRACE: calling {func.__name__}()'
              f'with {args},{kwargs}')
        original_result = func(*args,**kwargs)
        print(f'TRACE: {func.__name__}()'
              f'returned {original_result !r}')
        return original_result
    return wrapper

import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

def foo(required, *args,**kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

def foo2(x,*args,**kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra',)
    bar(x,*new_args,**kwargs)

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.color = 'blue'

AlwaysBlueCar('green',48392).color

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args,**kwargs):
        print(f,args,kwargs)
        result = f(*args,**kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting,name):
    return '{}, {}!'.format(greeting,name)

genexpr = (expression for item in collection)
def generator():
    for item in collection:
        yield expression


def build_person(first_name,last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name,'last': last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)
