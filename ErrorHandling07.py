import sys
a = int(input("enter first number : "))
b = input("Enter second number : ")
try:
    divide = a/b
    print("divide = ",divide)
except:
    print("Oops exception exception occurred due to line no.",sys.exc_info()[2].tb_lineno)
else:
    print("try over sucessfully")
    print("***The end***")

