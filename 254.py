import os
this_dir = os.getcwd()
print(this_dir)

os.chdir('..')

import platform
print(os.name)
print(platform.system())
print(platform.release())

