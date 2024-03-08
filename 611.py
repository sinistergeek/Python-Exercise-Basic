def evil_func(x):
    x[0] = 0

k = [1,2,3]
evil_func(list(k))
print(k)
