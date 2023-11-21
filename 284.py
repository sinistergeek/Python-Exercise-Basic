class Person():
    def __init__(self,given_name):
        self.name = given_name

if __name__ == '__main__':
    p1 = Person("Joe")
    print(p1)
    print(p1.__class__.__name__)
    print(p1.name)

    p2 = Person("Jane")
    print(p2)
    print(p2.name)

    p1.name = "Josepth"
    print(p1)
    print(p1.name)
