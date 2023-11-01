import sys
a = int(input("Enter first number : "))
b = input("Enter the second number : ")
try:
    divide = a/b
    print("try block over")
    print("divde = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception ocurred due to ",sys.exc_info()[2])
    print("***The ENd***")
