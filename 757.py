from collections import defaultdict
from typing import(
    Iterable,Callable,Dict,List,TypeVar,
    Iterator,Tuple,cast)
D_ = TypeVar("D_")
K_ = TypeVar("K_")

def partitionn(
        source: Iterable[D_],
    key: Callable[[D_],K_] = lambda x:cast(K_,x)
    ) -> Iterable[Tuple[K_,Iterator[D_]]]:
    pd: Dict[K_,List[D_]] = defaultdict(list)
    for item in source:
        pd[key(item)].append(item)
    for k in sorted(pd):
        yield k, iter(pd[k])

