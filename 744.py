from PIL import Image
from typing import Iterable, Tuple
Point = Tuple[int,int]
RGB = Tuple[int,int,int]
Pixel = Tuple[Point,RGB]
def pixel_iter(img:Image) -> Iterator[Pixel]:
    w, h  = image.size 
    return(
        (c,img.getpixel(c))
        for c in product(range(w),range(h))
    )
