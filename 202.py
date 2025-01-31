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
