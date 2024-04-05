import math
def isprimeh(x: int) -> bool:
    if x == 2: return True
    if x % 2 == 0 : return False
    factor = first(lambda n : x%n == 0,range(3,int(math.sqrt(x) + .5) +1,2))
    return factor is None
