from typing import Callable, Iterable, Any
def sum_f(
        function: callable[[Any],float],
        data: Iterable) -> float:
    return sum(function(x) for x in data)
