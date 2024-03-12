def fibonacci(n):
    if n == 0:
        x = 0
    elif n==1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
    return x
print(fibonacci(8))
