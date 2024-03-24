def shifty(b: int) -> int:
    return 1 << b

def multy(b: int) -> int:
    if b == 0: return 1
    return 2*multy(b-1)

def faster(b: int) -> int:
    if b == 0: return 1
    if b%2 == 1: return 2*faster(b-1)
    t = faster(b//2)
    return t*t
