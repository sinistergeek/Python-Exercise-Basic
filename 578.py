import re
number = "123.12"
m = re.match(r'(?P<Expotent>\d+)\.(?P<Fraction>\d+)',number)
if m:
    print("m.groupdict(): ",m.groupdict())
else:
    print("No match!")
