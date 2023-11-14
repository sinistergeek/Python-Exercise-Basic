import re
s = "Python exercises consist of various Modules."
result = re.match("Python",s)
print(result.group())
