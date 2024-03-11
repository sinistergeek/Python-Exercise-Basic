def factorial(n):
    if n>1:
        x=n*factorial(n-1)
    else:
        x=1
    return x
print(factorial(6))
