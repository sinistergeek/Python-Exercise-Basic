from typing import Callable,Iterable, Any
def map_reduce(
        map_fun: Callable,
        reduce_fun: Callable,
        source: Iterable
    )-> Any:
    return reduce(reduce_fun,map(map_fun,source))
