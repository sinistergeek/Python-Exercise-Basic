def alphabet():
    for c in 'abcde':
        yield c

g = alphabet()
x = next(g)
print(x)

x = next(g)
print(x)
