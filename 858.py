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
