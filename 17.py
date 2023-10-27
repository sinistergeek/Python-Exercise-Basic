def ODDorEVEN(x):
    """This is a function to determine
    whether a number is even or odd"""
    if(x%2==0):
        print(x,"is an even number.")

    else:
        print(x, "is an odd number.")
    return
x=eval(input("Enter a number to evaluate: "))
ODDorEVEN(x)
