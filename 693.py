from predicative_dispatch import predicate

@predicate(lambda x: x < 0, lambda y: True)
def sign(x,y):
    print("x is negative; y is",y)

@predicate(lambda x: x == 0, lambda y: True)
def sign(x,y):
    print("x is zero; y is",y)

@predicate(lambda x: x > 0, lambda y: True)
def sign(x,y):
    print("x is positive; y is ", y)
