def fun1():
    v= "Andy"
    def fun2():
        nonlocal v 
        v = "Rose"
    fun2()
    return v 
print(fun1()

class Animal:
      count = 88 
      def __init__(self,value1,value2):
        self.name = value1 
        self.age = value2 
      def show(self):
      print("The animal name is "+self.name)
      print("The tiger age is "+self.age)

tiger = Animal("Tiger","100")
tiger.show()
print("Tiger counts" + str(tiger.count))

myObj = object()
print(dir(myObj))

f = open("myfile.txt","a")
f.write("Hello World!")
f.close()
f = open("myfile.txt","r") 
print(f.read())

f = open("myfile.txt","w")
f.write("Hello World!")
      f.close()
      f = open("myfile.txt","r")
      print(f.read())
integers = range(8)
squared = (i * i for in integers)
negated = (-i for i in squared)
