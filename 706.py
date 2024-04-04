from numbers import Number
from typing import Callable, Iterator

Num_Conv = Callable[[str],Number]

def numbers_from_rows(conversion: Num_Conv,text:str) -> Iterator[Number]:
    return(conversion(value) 
           for line in text.splitlines()
           for value in line.split())
