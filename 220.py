import re

text = 'The black cat climed'
match = re.search(r'lac',text)
if match:
    print("Matching")
    print(match.group(0))

match = re.search(r'dog',text)
if match:
    print("Matching")
else:
    print("Did no match")
    print(match)
