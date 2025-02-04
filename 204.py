english = set(['door','car','lunar','era'])
spanish = set(['era','lunar','hola'])

print('english: ',english)
print('spanish: ',spanish)

both = english.intersection(spanish)

print(both)
print('issubset: ', both.issubset(english))
print('issubset: ', both.issubset(spanish))

diff = english.symmetric_difference(spanish)
print('symmetric_difference: ',diff)


all_the_words = english.union(spanish)
print(all_the_words)

from car import Car, ElectricCar

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_mustang = Car('ford','mustang',2024)
print(my_mustang.getdescriptive_name())
my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
