from typing import Iterator, Tuple, Text, Iterable
Text_Iter = Iterable[Tuple[Text,Text]]
LL_Iter = Iterable[Tuple[float, float]]
def float_from_pair(lat_lon_iter: Text_Iter) -> LL_Iter:
    return (
            (float(lat),float(lon))
            for lat,lon in lat_lon_iter
            )

legs(
        float_from_pair(
            lat_lon_kml(
                row_iter_kml(source))
            )
        )
