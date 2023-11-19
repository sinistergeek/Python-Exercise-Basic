import re

line1 = 'There is a phone number 12345 in this row and another 42 number'
numbers1 = re.findall(r'\d+',line1)
print(numbers1)

line2 = 'There are no numbers row. Not even one.'
number2 = re.findall(r'\d=',line2)
print(number2)
