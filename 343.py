numbers = [1,3,27,10,38]
def big(n):
    return n>10
reduced = filter(big,numbers)
print(reduced)
print(list(reduced))
