class Foo:
    @staticmethod
    def bar():
        print('Static method bar()')
    @staticmethod
    def stat():
        print("Static method stat()")
    def class1(self,string_a):
        print(string_a)

#Calling static method bar()
Foo.bar()

#Calling static method stat()
Foo.stat()

#Calling bounded method class1()
f = Foo()

#Calling bounded method class1()
f = Foo()
f.class1('bounded method')
