import os
src = 'myfile.txt'
dst = 'histfile.txt'
os.link(src,dst)
print("Create a hard link successfully!")
