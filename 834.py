myDict = {0:"apple",1:"banana",2:"cherry"}
removed_item = myDict.pop(1)
print(removed_item)


student = {"name":"Andy","age":"17","id":"0026"}
print("The removed item is:"student.popitem())


dict1 = {0:"apple",1:"banana",2:"cherry"}
dict2 = {1:"berry",2:"cashew"}
dict1.update(dit2)
print("dict1 =",dict1)

dict = {'ant':1,"bee":2,'cat':3}
print(dict.values())

set1 = {"ant","bee","cat"}
set2 = {"ant","bee","cow"}
diff = set1.difference(set2)
print(diff)
