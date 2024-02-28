#adding the result of func
class database:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        total_call = self.x + other.x
        total_call1 = self.y + other.y
        dail = database(total_call,total_call1)
        return dail
    def __str__(self):
        return str(self.x) + ":" + str(self.y)
    
callme = database(44,22)
callme2 = database(2,34)
dail = callme + callme2
print(dail)
