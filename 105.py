class ClassOne(object):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def square(self,p3):
        print(p3**2)

p = ClassOne(1,2)
print(hasattr(p,'p2'))
