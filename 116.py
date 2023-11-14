class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} - {self.age}'

p1 = Person('Tom',34)
p2 = Person('Alice',28)
p3 = Person('John',37)
arr = [p1,p2,p3]
tee = arr.sort(key = lambda x: x.age,reverse=True)
print(Person.__repr__)
