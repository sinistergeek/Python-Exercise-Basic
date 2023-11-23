from functools import reduce


numbers = [2,1,4,3]

print(reduce(lambda x,y:x if x < y else y, numbers))
print(reduce(lambda x,y:x if x > y else y, numbers))

n = 4
print(reduce(lambda x,y: x*y, range(1,n+1),1))

a = [1,3,6]
b = [2,4,5]
c = map(lambda x,y:x if x > y else y,a,b)
print(list(c))
