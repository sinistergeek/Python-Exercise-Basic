x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
try:
    divide = x/y
    print("try block over")
    print("divide = ",divide)
except ZeroDivisionError:
    print("OOPS except occured due to Zero dvision error")
    print("****THE enD7***8")
