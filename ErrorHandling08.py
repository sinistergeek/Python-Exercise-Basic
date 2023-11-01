a = int(input("Enter first number : "))
b = int(input("Enter second number :"))
try:
    divide = a/b
    print("divide = ",divide)
except:
    print("OOPS exception occurred due to line no.",sys.exc_info()[2].tb_lineno)
else:
    print("try over successfully")
    print("***THE END***")

