import re

line = "Learn to Analyze Data with Scientific Python"

m = re.search(r'(.*) to (.*?) .*',line,re.M|re.I)

if m:
    print("m.group() :",m.group())
    print("m.group(1) :",m.group(1))
    print("m.group(2) :",m.group(2))

else:
    print("No match!!")
