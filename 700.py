from ch02_ex3 import (lat_lon_kml, float_from_pair,haversine)

path = tuple(float_from_pair(lat_lon_kml()))
distances_1 = map(
        lambda s_e: (s_e[0],s_e[1],haversine(*s_e)),zip(path,path[1:])
        )
