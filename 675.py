import xml.etree.ElementTree as XML

from typing import Text, List, TextIO, Iterable 
def row_iter_kml(file_obj: TEXTIO) -> Iterable[List[Text]]:
    ns_map={
            "ns0":"http://www.opengis.net/kml/2.2",
            "ns1":"http://www.google.com/kml/ext/2.2"
            }
    path_to_points = ("./ns0:Document/ns0:Folder/ns0:Placemark/"
                      "ns0:Point/ns0:coordinates")
    docs =XML.parse(file_obj)
    return (comma_split(Text(coordinates.text))
            for coordinates in
            doc.findall(path_to_points, ns_map))
