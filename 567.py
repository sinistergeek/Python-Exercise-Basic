class A:
    def f1(self):
        print("In a f1")
class B:
    def f2(self):
        print("In a f2")

class C(A,B):
    def f3(self):
        print("in C f3")

obj1 = C()
obj1.f1
obj1.f2
obj1.f3
