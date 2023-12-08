import keyword
print(keyword.kwlist)


x = """
This is a multiline string that spans multiple lines
"""
print(x)


import sys

print("Command line arguments:",sys.argv)
print("First argument:", sys.argv[1])
print("Second argument:", sys.argv[2])
