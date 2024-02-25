def tail(x):
    if x:
        del x[0]
k = [1,2,3]
tail(k)
print(k)
