import re

match = re.search(r'xa*','xaaab')
print(match.group(0))

match = re.search('xa*','xabxaab')
print(match.group(0))

match = re.search('a*','xabxaab')
print(match.group(0))

match = re.search(r'a*','aaaxabxaab')
print(match.group(0))
