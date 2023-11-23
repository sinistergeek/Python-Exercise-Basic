from functools import reduce

numbers = [1,2,3,4]
print(reduce(lambda x,y: x+y,numbers))
print(reduce(lambda x,y: x*y,numbers))
print(reduce(lambda x,y: x/y,[8,4,2]))

print(reduce(lambda x,y: x+y,[2]))

print(reduce(lambda x,y: x+y,[],0))
print(reduce(lambda x,y: x+y,[2,4],1))

mysum = 0
for num in numbers:
    mysum += num

print(mysum)

mymultiple = 1

for  num in numbers:
    mymultiple *= num
print(mymultiple)
