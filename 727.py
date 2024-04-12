from typing import cast, TextIO, Tuple, Iterator, List
from Chapter_6.ch06_ex3 import row_iter_kml
from Chapter_4.ch04_ex1 import legs, haversine


source = "file:./Winter%202012-2013.kml"
def get_trip(url: str=source) -> List[Leg]:
    with urllib.request.urlopen(url) as source:
        path_iter = float_lat_lon(row_iter_kml(cast(TextIO,source)))
        pair_iter = legs(path_iter)
        trip_iter = (
        Leg(start,end,round(haversine(start,end),4))
        for start, end in pair_iter
                )
    return trip
