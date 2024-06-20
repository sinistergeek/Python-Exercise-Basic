os.chdir("c:\\mydir")
cwd = os.getcwd()
print("The current working directory is:",cwd)

c= char(86)
print(c) 


class Animal:
    count = 88
    def __init__(self,value1,value2):
        self.name = value1 
        self.age = value2 

    def show(self):
        print("The animal name is"+ self.name)
        print("The tiger age is"+ self.age) 
tiger = Animal("Tiger","100")
tiger.show()
print("Tiger counts"+str(tiger.count))
