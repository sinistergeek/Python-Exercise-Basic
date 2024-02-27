class Person:
    def __init__(self):
        self.age = __age #private method

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age

p1 = Person()
p1.set_age(19)
print(p1.__age)
