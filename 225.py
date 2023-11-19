import re

line = 'There is phone number 12345 in this row and another 42 number'
match  = re.search(r'\w+ \d+',line)
if match:
    print(match.group(0))
match = re.search(r'\w+ (\d+)',line)
if match:
    print(match.group(0))
    print(match.group(1))
matches = re.findall(r'\w+ \d+',line)
print(matches)

matches = re.findall('\w+ (\d+)',line)
print(matches)
