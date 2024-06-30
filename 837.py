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

str = "Perl in 8 Hours!"
s = str.endswith("!")
print(s)

m = ('ant','bee','cat')
n = enumerate(m)
print(list(n))

try:
    value = 100/0 
except:
    print("Error Occours!")

