from typing import Callable, Iterable, Tuple, Iterator

Point = Tuple[float, float]
Leg_Raw = Tuple[Point, Point]
Point_Func = Callable[[Point, Point],float]
Leg_D = Tuple[Point,Point,float]

def cons_distance(
    distance: Point_Func,
    legs_iter: Iterable[Leg_Raw]) -> Iterator[Leg_D]:
    return(
            (start, end, round(distance(start,end),4))
            for start,end in legs_iter
        )
