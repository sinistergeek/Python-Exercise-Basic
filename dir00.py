import os

pathlocation = os.getcwd()
booleanVal = os.path.exists(pathlocation)
if (booleanVal == True):
    print('File path exist {}'.format(pathlocation))
else:
    print('File path doesnt exist')

