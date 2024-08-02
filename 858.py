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

