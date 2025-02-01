counter = {}
word = 'eggplant'
if word not in counter:
    counter[word] = 0
counter[word] += 1
print(counter)

class ElectricCar(Car):
    """ Represent aspects of a car, specific to elelctric vehicles."""

    def __init__(self,make,model,year):
        """ Initialize attributes of the parent class."""
        super().__init__(make,model,year)

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())

class Battery:
    """ A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the batteryt size."""
        print(f"This car has a  {self.battery_size}-kWh battery.")
