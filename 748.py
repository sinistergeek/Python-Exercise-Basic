from functools import total_ordering
from numbers import numbers
from typing import NamedTuple

@total_ordering
class Card2(NamedTuple):
    rank:int
    suit: str
    def __eq__(self,other:Any) -> bool:
        if isinstance(other,Card2):
            return self.rank == other.rank
        elif isinstance(other,int):
            return self.rank == other
        return NotImplemented
    def __lt__(self,other: Any) -> bool:
        if isinstance(other,Card2):
            return self.rank<other.rank
        elif isinstance(other,int):
            return self.rank < other
        return NotImplemented
