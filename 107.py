class ClassOne(object):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def square(self,p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self,x):
        print(x * 10)

y = ClassTwo(10,20)
print(y.p1)
