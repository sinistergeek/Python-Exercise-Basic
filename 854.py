import os
src = 'myfile.txt'
dst = 'histfile.txt'
os.link(src,dst)
print("Create a hard link successfully!")

mylist=["a","b","c","d"]
print(mylist)

myList = ['ant','bee','cat']
myList.append('dog')
print(myList)

myList = [1,2,3,4,5]
myList.clear()
print('myList=',myList)

unprinted_designs = ['phone case', 'robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

class Dog:
    """ A simple attempt to model a dog."""

    def __init__(self,name,age):
        """ Intialize name and age attributes """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
