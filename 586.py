import re
line = "Learn to Analyze Data with Scientific Python"
m = re.search(r'(python)',line,re.M|re.I)
if m:
    print("m.group() ",m.group())
else:
    print("No match by obj.search!!")
    
m = re.search(r'(python)',line,re.M|re.I)
if m:
    print("m.group() :",m.group())
else:
    print("No match by obj.match")
