english = set(['door','car','lunar','era'])
spanish = set(['era','lunar','hola'])

print('english: ',english)
print('spanish: ',spanish)

both = english.intersection(spanish)

print(both)
print('issubset: ', both.issubset(english))
print('issubset: ', both.issubset(spanish))

diff = english.symmetric_difference(spanish)
print('symmetric_difference: ',diff)


all_the_words = english.union(spanish)
print(all_the_words)
