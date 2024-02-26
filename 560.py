def addn(n):
    def add(x):
        return x + n
    return add

a = [1,3,0,6]
b = map(addn(1),a)
print(list(b))
