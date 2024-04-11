from typing import NamedTuple
class Point(NameTuple):
    latitude: float
    longitude: float

class Leg(NamedTuple):
    start: Point
    end: POint
    distnace: float
