import sys
import module

files = sys.argv[1:]
for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError:
        print("Cannot divide by 0 in file {}".format(filename))
    except IOError:
        print("Cannot open file {}".format(filename))

