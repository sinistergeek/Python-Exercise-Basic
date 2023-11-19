import os, sys
print(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

mypath = os.path.join(project_root,'lib')
print(path)
sys.path.insert(0,mypath)

