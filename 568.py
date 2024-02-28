class A:
    def __init__(self):
        self.m1 = 9

class B(A):
    def __init__(self):
        super().__init__()
        self.m2 = 8
d1 = B()
print(d1.m1)
print(d1.m2)
