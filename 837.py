import json 
p = {"name":"Andy","age":"18","id":"007"}
j = json.dumps(p)
print(j)


from collections import Counter 
obj = Counter("cheatsheet")
for item in obj.elements():
    print(item)


import demjson
json = demjson.encode(dict)

