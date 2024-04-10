from typing import NamedTuple
class Color(NamedTuple):
    red: int
    blue: int
    green: int
    name: str
def color_palette(
    headers: Tuple[str,str],
    row_iter: Iterator[List[str]]
    ) -> Tuple[str,str,Tuple[Color,...]]:
    name,columns = headers
    colors = tuple(
            Color(int(r),int(g),int(b),"".join(name))
            for r,g,b *name in row_iter)
    return name, columns, colors
