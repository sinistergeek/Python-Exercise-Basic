import re

line = 'There is a phone number 1234 in this row and an age: 23'

match = re.search(r'd+',line)
if match:
    print(match.group(0))
