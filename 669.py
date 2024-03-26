def pfactorsl(x:int) -> Iterator[int]:
    if x % 2 == 0:
        yield 2
        if x//2 > 1:
            yield from pfactorsl(x//2)
        return
    for i in range(3,int(math.sqrt(x) + .5)+1,2):
        if x % i == 0:
            yield i 
            if x // i > 1:
                yield from pfactorsl(x//i)
            return
    yield x
