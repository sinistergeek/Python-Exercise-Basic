class ClassOne(object):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def square(self,p3):
        print(p3**3)

class ClassTwo(ClassOne):
    def times10(self,x):
        return x * 10

obj = ClassTwo(15,25)
print(obj.times10(45))
