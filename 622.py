import math

k = [1,4,-2,16,-3,36,-1]
f = filter(lambda x: x>=0, k)
m = map(math.sqrt,f)
print(list(m))
