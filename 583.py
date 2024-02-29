import re

number = "124.13"
m = re.search(r'(?P<Expotent>\d+)\.(?P<Fraction>\d+)',number)
if m:
    print('m.groupdict() :',m.groupdict())
else:
    print("No match!!")
