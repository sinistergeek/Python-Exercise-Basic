from copy import deepcopy
x = ['apple','bob','cat','drone']
y = deepcopy(x)

x[0] = 'qqrq'
print(x)
print(y)
