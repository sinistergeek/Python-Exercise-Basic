a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
except (ZeroDivisionError,TypeError) :
    print("OOPS exception occurred due to Exception")
    print("***THE END***")
