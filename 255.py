import os
import sys

if len(sys.argv) != 2:
    exit("Usage: {} PATH_TO_DIRECTORY".format(sys.argv[0]))

root = sys.argv[1]

for dirname,dirs,files in os.walk(root):
    for filename in files:
        print(os.path.join(dirname,filename))


