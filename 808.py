def fact(n: int) -> int:
    if n == 0: return 1
    else: return n*fact(n-1)


def facti(n:int) -> int:
    if n == 0: return 1 
    f = 1 
    for i in range(2,n):
        f = f * i
    return f
