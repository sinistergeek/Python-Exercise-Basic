def square(x):
    print('Evaluating square',x)
    return x*x
a = [2,5,6]
print('Calling map')
m = map(square,a)
print('called map')
print('Entering loop')
for x in m:
    print('Start of loop body')
    print(x)
