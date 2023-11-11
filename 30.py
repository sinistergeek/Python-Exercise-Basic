class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def __repr__(self):
        return f"Person(fname='{self.fname}',lname='{self.lname}')"
person = Person('Mike','Smith')
print(person)
