english = set(['door','car','lunar','era'])
spanish = set(['era','lunar','hola'])

print('english: ',english)
print('spanish: ',spanish)
both = english.intersection(spanish)
print(both)
print('issubset: ', both.issubset(english))
print('issubset: ', both.issubset(spanish))
