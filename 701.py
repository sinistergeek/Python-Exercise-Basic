def myfilter(f,C):
    for x in C:
        if f(x):
            yield x

myfilter(f,C)
