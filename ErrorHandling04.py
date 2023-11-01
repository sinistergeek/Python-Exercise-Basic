import sys
a=int(input("Enter first number : "))
b=input("Enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception occurred due to ",sys.exc_info()[1])
    print("***THE END***")
