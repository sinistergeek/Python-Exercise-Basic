names = ['Jan','Feb','Mar','Apr']
days = [31,28,31,30]

zipped = zip(names,days)
print(zipped)

pairs = list(zipped)
print(pairs)

month = dict(zipped)
print(month)

zipped = zip(names,days)
moth = dict(zipped)
print(moth)
