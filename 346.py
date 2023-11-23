numbers = [1,8,10,57,12,8]
def big(x):
    print(f"filtering {x}")
    return x > 10
def double(y):
    print(f"double {y}")
    return 2*y
for num in map(double,filter(big,numbers)):
    print(num)
