import itertools
from typing import Iterable, Any
def imits(iterable: Iterable[Any]) -> Any:
    max_tee, min_tee = itertools.tee(iterable,2)
    return max(max_tee), min(min_tee)
