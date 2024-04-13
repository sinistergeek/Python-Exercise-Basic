from typing import Iterable, Iterator
def rank_y(pairs: Iterable[Pair]) -> Iterator[RankedPair]:
    return enumerate(sorted(pairs, key=lambda p: p.y))

Rank2Pair = Tuple[int, RankedPair]
def rank_x(
            ranked_pairs: Iterable[RankedPair]
            ) -> Iterator[Rank2Pair]:
    return enumerate(
                sorted(ranked_pairs, key=lambda rank: rank[1].x)
            )
