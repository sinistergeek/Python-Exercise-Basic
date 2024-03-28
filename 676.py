from typing import Text, List, Iterable
Rows = Iterable[List[Text]]
LL_Text = tuple[Text,Text]
def lat_lon_kml(row_iter: Rows) -> Iterable[LL_Text]:
    return (pick_lat_lon(*row) for row in row_iter)
url = "file:./Winter%202012-2013.kml"
with urllib.request.urlopen(url) as source:
    v1= tuple(lat_lon_kml(row_iter_kml(source)))
print(v1)
