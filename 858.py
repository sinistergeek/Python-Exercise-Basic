os.chdir("c:\\mydir")
cwd = os.getcwd()
print("The current working directory is:",cwd)

os.chdir("c:\\mydir")
cwd = os.chdir()
print("The current working directory is:",cwd)

import os
path="/"
contents = os.listdir(path)
print("The directories and files in''', path,''':")
print(contents)

class Computer:
    def __init__(self,name):
        self.name = name 
    def capacity(self,harddrive,memory):
        self.harddrive = harddrive 
        self.memeory = memeory 
class Laptop(Computer):
    def capacity(self,harddrive,memory):
        print(self.name)
        print("Harddrive capcity:" + str(harddrive))
        print("Memory capacity:" + str(memory))
L = Laptop("Laptop")
L.capcity(8000,6)

str = "Visual Basic in 8 Hours"
s = str.partition("in")
print(s)

num = 100 
if nm > 100:
    pass 
print('Here has a placeholder for future code')

import re 
print(re.match('ray','ray@yahoo.com').span())

x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

import random 
print(random.randrange(1,10)

txt = "The best things in life are free!"
if "free" in txt:
      print("Yes,'free' is present.")


class myclass():
      def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myFunction():
      return True 
if myFunction():
      print("YES!")
else:
      print("NO")

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
      print("Yes, 'apple' is in the fruits list")


thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple) 
print(thislist)
