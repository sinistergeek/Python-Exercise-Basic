def evil_func(x):
    x[0] = 0
t = (1,2,3)
evil_func(t)
print(t)
