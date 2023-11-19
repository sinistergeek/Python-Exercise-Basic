import re

text = "This is <a string> with some sections <marked> with special character"
m = re.search(r'<[^>]*>',text)
if m:
    print(m.group(0))
