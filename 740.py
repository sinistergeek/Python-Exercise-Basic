from typing import NamedTuple,Iterator

class Point(NamedTuple):
    latitude: float
    longitude: float

class Leg(NamedTuple):
    start: Point
    end: Point
    distance: float
def ordered_leg_iter(
        pair_iter: Iterator[Tuple[Point,Point]]
    ) -> Iterator[Leg]:
    for order, pair in enumerate(pair_iter):
        start,end = pair
        yield Leg(
            order,
            start,
            end,
            round(haversine(start,end),4)
        )
