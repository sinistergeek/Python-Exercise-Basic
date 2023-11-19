import re

line = "abc123def"

print(re.sub(r'\d+',' ',line))
print(line)

print(re.sub(r'x','y',line))
print(line)

print(re.sub(r'([a-z]+)(\d+)([a-z]+)',r'\3\2\1', line))

print(re.sub(r'''([a-z]+)([a-z]+)''', r'\3\2\1', line, flags=re.VERBOSE))
print(re.sub(r'...',line))
print(re.sub(r'...','x', line))


print(re.sub(r'(.)(.)',r'\2\1', line))
