class MyClass:
    def __init__(self):

        print("Constructor is called")
    def __del__(self):
        print("Destructor is called")

obj = MyClass()
del obj

