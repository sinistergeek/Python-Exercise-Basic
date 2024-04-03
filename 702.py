from typing import Callable, Iterable, Tuple, Iterator, Any

Conv_F = Callable[[float],float]
Leg = Tuple[Any, Any, float]

def convert(
        conversion: Conv_f,
        trip: Iterable[Leg]) -> Iterator[float]:
    return(
            conversion(distance) for start, end, distance in trip
        )
