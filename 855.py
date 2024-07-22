import os 
path="/"
contents = os.listdir(path) 
print("THe directories and files in ",path, "":")
print(contents)

str = "This is a left-adjust example."
print(str.ljust(40,'$'))

import json 
j = '{"name":"Andy","age":18,"id":"007"}'
p = json.loads(j)
print(p)
