import sys

s = sys.argv[1]
unique = ''
for c in s:
    print(c)
    if s not in unique:
        unique += c
print(len(unique))
