from typing import Callable, Sequence, Any
def mapr(f: Callable[[Any],Any],
         collection: Sequence[Any]) -> List[Any]:
    if len(collection) == 0: return []
    return mapr(f,collection[:-1]) + [f(collection[-1])]
