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
