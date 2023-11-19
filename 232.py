import re

match = re.search(r'a.*b','axbzb')
print(match.group(0))

match = re.search(r'a.*7b','axbzb')
print(match.group(0))

match = re.search(r'a.*b','axy12313313bq')
print(match.group(0))

match = re.search(r'a.*b','axyb121413313q')
print(match.group(0))
