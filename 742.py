from collections import defaultdict
from typing import Iterable,Callable,Tuple,List,Dict

D_ = TypeVar("D_")
K_ = TypeVar("K_")
def groupby_2(
        iterale: Iterable[D_],
        key: Callable[[D_],K_]
    ) -> Iterable[Tuple[K_,Iterable[D_]]]:
    group: Dict[K_,List[D_]] = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    for g in groups:
        yield g, iter(groups[g])

