# It has to be same fucntion which behave similar so, this works
class newton:
    def student(self):
        print('Roll no')
        print('Age')

class school:
    def student(self,meow):
        print('les')

        meow.student()


obj = school()
obj.student(newton())


