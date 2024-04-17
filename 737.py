from typing import Callable, Iterator, TypeVar 
T_ = TypeVar("T_")
def until(
        terminate: Callable[[T_],bool],
        iterator: Iterator[T_]
    ) -> T_:
    i = next(iterator)
    if terminate(i):
        return i
    return until(terminate,iterator)
