import re

def regex_processor(line):
    m = re.match(r'(.*) to (.*?) .*',line,re.M|re.I)
    if m:
        print(m.group(0))
    else:
        print("No Match!!")
