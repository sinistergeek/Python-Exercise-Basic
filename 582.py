import re

line = "learn Data, Python"
m = re.search(r'(\W+)(\W+)', line,re.M|re.I)
if m:
    print("m.group():",m.group())
    print("m.group(1,2):",m.group(1,2))
else:
    print("No match!")
