class student:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        total = self.x + other.x
        total1 = self.x + other.x
        ob3 = student(total,total1)
        return ob3

    def __str__(self):
        return str(self.x) + ":" + str(self.x)


ob1 = student(33,34)
ob2 = student(99,133)
ob3 = ob1 + ob2

print(ob3)

