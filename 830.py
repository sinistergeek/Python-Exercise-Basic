import itertools
import operator
fruit = ['apple','banana','cherry','date']
select = [False,False,True,False]
favorite = itertools.compress(fruit,select)
for item in favorite:
    print("My favorite fruit is: ",item)
