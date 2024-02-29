import re
email = "hello@leremove_thisarntoalayzedata.com"
m = re.search("remove_this",email)

if m:
    print("email address :",email[:m.start()] + email[m.end():])
else:
    print("No match!!")
