class Person:
    def __init__(self):
        self.age = None
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age

p1 = Person()
p1.set_age(19)
print(p1.get_age())
