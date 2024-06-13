class MyClass(object):
    def __new__(cls):
        print("Create new class instance")
        return super(MyClass,cls).__new__(cls)
    def __init__(self):
        print("__init__() is called")

MyClass()
