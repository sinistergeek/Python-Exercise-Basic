import json
p = {"name":"Andy","age":18,"id":"007"}
j = json.dumps(p)
print(j)

k = '{"name":"Andy","age":18,"id":"007"}'
l  = json.loads(j)
print(l)
