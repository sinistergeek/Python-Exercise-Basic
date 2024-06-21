class Computer:
    harddrive = 1000
    memory = 8
    def setValue(self,harddrive,memory):
        Computer.harddrive = harddrive 
        Computer.memory = memory 

class Desktop(Computer):
    def capacity(self):
        print("Harddrive capacity: " + str(self.harddrive))
        print("Memory capacity: " + str(self.memory))

D = Desktop()
D.setValue(9000,7)
D.capacity()
