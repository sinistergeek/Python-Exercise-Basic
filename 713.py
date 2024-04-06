from typing import Callable, Iterable, Iterator, Any, TypeVar
D_ = TypeVar("D_")
R_ = TypeVar("R_")
def mapf(
        f: Callable[[D_],R_],
        C: Iterable[D_]
        ) -> Iterator[R_]:
    return (f(x) for x in C)
