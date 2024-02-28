import re
#re.match()
#re.search()
#re.split()
#re.sub()
#re.findall()
#re.compile()

line = "Learn to Analyze Data with scientific Python"
m = re.match(r'(.*) to (.*?).*',line,re.M|re.I)

if m:
    print("m.group():",m.group())
    print("m.group(1):",m.group(1))
    print("m.group(2):",m.group(2))
else:
    print ("No match")

