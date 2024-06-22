import re 
pattern = re.compile("^(\d{3})-(\d{3})-(\d{4})$")
phoneNumber = input("Enter your phone number:")
valid = pattern.match(phoneNumber)
print(phoneNumber)
if valid:
    print("Valid Phone NUmber!")
