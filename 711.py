def fastexp(a: float, n: int) -> float:
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a*fastexp(a,n-1)
    else:
        t= fastexp(a,n//2)
        return t*t
