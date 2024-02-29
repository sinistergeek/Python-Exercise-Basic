import re

def regex_processor(email):
    m = re.match("take_out",email)

    if m:
        print(email[:0] + email[0:])
    else:
        print("No match!!")
