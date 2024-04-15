from typing import NamedTuple
class Ranked_Y(NamedTuple):
    r_y: float
    raw: Pair 

def rank_y(pairs: Iterable[Pair]) -> Iterable[Ranked_Y]:
    return(
        Ranked_Y(rank,data)

        for rank, data in rank(pairs, lambda pairs: pair.y)
    )
