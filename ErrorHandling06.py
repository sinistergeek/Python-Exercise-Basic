import sys
a = int(input("Enter first number : "))
b = input("Enter Second number")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception occurred due to line no.",sys.exc_info()[2].tb_lineno)
    print("***THE END***")
