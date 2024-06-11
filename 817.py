class MyClass:
    def __format__(self,myFormat):
        if myFormat == 'No good!': 
            return 'Very good!'
        return myFormat 
c = MyClass()
print(format(c,'No good!'))
