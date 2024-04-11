from typing import Tuple, Iterator, List

def float_lat_lon_tuple(
        row_iter: Iterator[List[str]]) -> Iterator[Tuple]:
    return(tuple(*map(float,pick_lat_lon(*row)))
           for row in row_iter)
