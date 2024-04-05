from typing import Callable, Iterable

class Sum_Filter:
    __slots__ = ["filter","function"]
    def __init__(self, filter: Callable[[Any],bool],
                 func: Callable[[Any],float]) -> None:
        self.filter = filter
        self.function = func

    def __call__(self,iterable: Iterable) -> float:
        return sum(
                self.function(x)
                for x in iterable
                if self.filter(x)
                )
