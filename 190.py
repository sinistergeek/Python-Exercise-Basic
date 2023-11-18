text = """
This is a very long text.
Ok, maybe it is not that long after all.
"""

count = {}

for char in text:
    if char == '\n':
        continue
    if char not in count:
        
        count[char] = 1
        print(count[char])
    else:
        count[char] += 1

for key in sorted(count.keys()):
    print("'{}' {}".format(key,count[key]))
