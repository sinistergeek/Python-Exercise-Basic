from copy import deepcopy

a = {'name':'foo bar','grades':{'math':70,'art':100,},'friends' : ['Mary','John','Jane','George']}

b = deepcopy(a)
a['grades']['math'] = 90
a['email'] = 'foobar@gmal.com'
print(a)
print(b)
