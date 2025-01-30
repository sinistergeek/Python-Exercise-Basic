student = {
        "name":"Andy",
        "id":"0026"
        }
print(student.get("id"))

class Student:
    name = "Andy"
    id = "0026"
print(getattr(Student,'id'))

os.chdir("c:\\mydir")
cwd = os.getcwd()
print("The current working directory is:",cwd)


def fun():
    global myVar
    myVar = "Cheat Sheet"
fun()
print("Html Css" + myVar)

class Car:
    def __init__(self,make,model,year):
        """ Initialize attributes to describes a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """ Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
