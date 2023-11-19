import re

strings = [

'99921-58-10-7',
'0-9752298-0-X',
'0000000000000',
'-------------',
'0-9752298-0-Y']

for isbin in strings:
    print(isbin)
    if (re.search('[\dX-]{13}$',isbin)):
        print("match 1")

    if(re.search(r'^\d{1,5}-\d{1,5}-[\dX]$',isbin) and len(isbin) == 13):
        print("match 2")
