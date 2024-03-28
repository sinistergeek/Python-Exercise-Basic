from typing import Iterator, Any
Item_Iter = Iterator[Any]
Pairs_Iter = Iterator[Tuple[float,float]]
def pairs(iterator: Iterm_Iter) -> Pairs_Iter:
    def pair_from(head: Any, iterable_tail: Iterm_Iter) -> Pairs_Iter:
        nxt = next(iterable_tail)
        yield head, next
        yield from pair_from(nxt, iterable_tail)
    try:
        return pair_from(next(iterator),iterator)
    except StopIteration:
        return iter([])
