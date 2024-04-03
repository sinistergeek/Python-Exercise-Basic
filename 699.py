from typing import Iterable, Any, Callable

def max_like(trip: Iterable[Any], key: Callable) -> Any:
    wrap = ((key(leg),leg) for leg in trip)
    return sorted(wrap)[-1][1]
