import re
line = "Learn Data, Python"
m = re.match(r'(\W+)(\W+)',line,re.M|re.I)
if m:
    print("m.group():",m.groups())
    print("m.group(1,2):",m.group(1,2))
else:
    print("No match!")

import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')
