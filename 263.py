import os
print(os.environ['Home'])
print(os.environ.ge('Home'))
for k in os.environ.keys():
    print("{:30} {}".format(k,os.environ[k]))

