def repeat(f,a):
    yield a
    for v in repeat(f,f(a)):
        yield v
