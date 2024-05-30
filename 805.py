from Chapter_3.ch03_ex5 import (
    series,head_map_filter,row_iter)
from typing import(
    NamedTuple,Callable,List,Tuple,Iterable,Dict,Any)
RawPairIter = Iterable[Tuple[float,float]]
class Pair(NamedTuple):
    x: float 
    y: float 
pairs: Callable[[RawPairIter],List[Pair]] \
    = lambda source: list(Pair(*row) for row in source)
def raw_data() -> Dict[str,List[Pair]]:
    with open("Anscombe.txt") as source:
        data = tuple(head_map_filter(row_iter(source)))
        mapping = {
            id_str: pairs(series(id_num,data))
            for id_num,id_str in enumerate(['I','II','III','IV'])
        }
    return mapping
