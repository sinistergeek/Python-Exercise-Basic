str = "Python"
print(str[2])

myString = "Python is a good language"
print(myString[7:16])

str = "abec"
print(str.index("e"))


class Computer:
    harddrive = 10000
    memory = 8
    def setValue(self,harddrive,memory):
        Computer.hardrive = harddrive
        Computer.memory = memory 
class Desktop(Computer):
    def capacity(self):
        print("harddrive capcity: "+ str(self.harddrive))
        print("Memory capcity: "+ str(self.memory))

D = Desktop()
D.setValue(900,7)
D.capacity
