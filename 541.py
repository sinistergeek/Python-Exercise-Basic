def squareN(n):
    if n == 1:
        return 1
    print(n)
    return n*n+squareN(n-1)
print(squareN(100))
