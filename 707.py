from typing import Iterator, Tuple

def group_by_iter(n: int, iterms: Iterator) -> Iterator[Tuple]:
    row = tuple(next(items) for i in range(n))
    while row:
        yield row
        row = tuple(next(items) for i in range(n))

group_by_iter(7,filter(lambda x: x%3==0 or x%5==0, range(100)))
