string = 'hello'

string = string.upper()
print(string)

string = string.lower()
print(string)

string = string.replace('l','L')
print(string)

string = 'edcorner,learning,cherry'
substrings = string.split(',')
print(substrings)

string = ' hello '
string = string.strip()
print(string)

string = 'hello'
print(string.startswith('he'))
print(string.startswith('ho'))


string = 'hello'
print(string.endswith('lo'))
print(string.endswith('lo'))


string = 'hello'
print('he' in string)
print('ho' in string)
