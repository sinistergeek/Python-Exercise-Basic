class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled 

ManglingTest().get_mangled()
ManglingTest().__mangled
