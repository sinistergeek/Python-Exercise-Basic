from operator import itemgetter
def semifact(n: int) -> int:
    alternatives = [
        (n == 0, lambda n: 1),
        (n == 1, lambda n: 1),
        (n == 2, lambda n: 2),
        (n > 2,lambda n: semifact(n-2)*n)
    ]
    _,f = next(filter(itemgetter(0),alternatives))
    return f(n)
