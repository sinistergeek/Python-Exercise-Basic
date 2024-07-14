from datetime import datetime 
now = datetime.now()
print(now.isoformat())

str="Scala in 8 Hours!"
s = str.isprintable()
print(s)

str = "   "
s = str.isspace();
print(s)

class Building:
    high = 100
class Room(Building):
    high = 5

print(issubclass(Room,Building))

set1 = {"ant","bee","cat"}
set2 = {"ant","bee","cat","dog","ewe"}
ss = set1.issubset(set2)
print(ss)
