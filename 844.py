def fun():
    global myVar
    myVar="Cheet Sheet"

fun()
print("Html Css" + myVar)


print(globals())

class Student:
    name = "Andy"
    id = "0026"
print(hasattr(Student,'id'))

str = 'Scala in 8 Hours'
print(hash(str))


help(list)