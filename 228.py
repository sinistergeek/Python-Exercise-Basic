import re

cases = ["hello","hello world.","hello, world","."]

for case in cases:
    print(case)
    match = re.search(r'.',case)
    if match:
        print(match.group(0))

print("------")

for case in cases:
    print(case)
    match = re.search(r'\.',case)
    if match:
        print(match.group(0))
print("-----")

for case in cases:
    print(case)
    match = re.search(r'[.]',case)
    if match:
        print(match.group(0))
