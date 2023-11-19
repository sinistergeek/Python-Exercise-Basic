import re

line = 'There is a phone number 12345 in this row and an age: 23'
match = re.search(r'((\w): (\d+))',line)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.groups())
