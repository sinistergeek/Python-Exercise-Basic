def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(result)
    finally:
        print("Execution complete")


divide(10,5)
