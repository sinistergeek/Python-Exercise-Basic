import re

line = 'There is a phone number 12345 in this row and another 42 number'

match = re.search(r'(\w+) (\d+)',line)

if match:
    print(match.group(1))
    print(match.group(2))

matches = re.findall(r'(\w+) (\d+)',line)
print (matches)
