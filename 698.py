from ch02_ex3 import(float_from_pair, lat_lon_kml, limits,haversine,legs)
path = float_from_pair(float_lat_lon(row_iter_kml(source)))
trip = tuple(start,end,round(haversine(start,end),4))
for start, end in legs(iter(path)))
