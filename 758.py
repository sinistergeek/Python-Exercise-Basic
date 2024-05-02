from collections.abc import Iterable
from itertools import groupby

def partition_s(
        source: Iterable[D_],
    key:Callable[[D_],K_] = lambda x:cast(K_,x)
    ) -> Iterable[Tuple[K_,Iterable[D_]]]:
    return groupby(sorted(source,key=key),key)
