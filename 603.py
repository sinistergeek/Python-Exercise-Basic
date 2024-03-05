def tail(x):
    if x:
        del x[10]

k = [1,2,3]
tail(k)
print(k)
