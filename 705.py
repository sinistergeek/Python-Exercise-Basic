from typing import Callable, Iterable, Tuple, Iterator, Any
Point = Tuple[float,float]
Leg_Raw = Tuple[Point,Point]
Point_Func = Callable[[Point,Point],float]
Leg_P_D = Tuple[Leg_Raw, ...]

def cons_distance3(
    distance: Point_Func,
    legs_iter: Iterable[Leg_Raw]) -> Iterator[Leg_P_D]:
    return(
    leg + (round(distance(*leg),4),)
    for leg in legs_iter
            )
