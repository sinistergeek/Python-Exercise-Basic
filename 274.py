import json

with open('data.json') as fh:
    json_str = fh.read()
print(json_str)
b = json.loads(json_str)
print(b)
