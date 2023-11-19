import re
s = 'Python'
if(re.search('python',s)):
    print('Python matched')

if (re.search('python',s,re.IGNORECASE)):
    print('Python matched with IGNORECASE)')
