class Student:
    school= "standard"

    def __init__(self):
        self.marks = 10
    def get_marks(self):
        return self.marks

    @classmethod
    def get_school(cls):
        return cls.school
    
    @staticmethod
    def add(x,y):
        return x+y

s1 = Student()
s2 = Student()

print(s1.get_marks())
print(s2.marks)
print(Student.get_school())
print(Student.add(3,5))
