from typing import(
    Callable, Sequence, Iterator, Union, Iterable,
    TypeVar,cast,Union
)
K_ = TypeVar("K_")
Source = Union[Rank_Data,Any]
def rank_data(
        seq_or_iter: Union[Sequence[Source],Iterator[Source]],
        key: Callable[[Rank_Data],K_] = lambda obj: cast(K_,obj)
    ) -> Iterable[Rank_Data]:
    if isinstance(seq_or_iter,Iteration):
        yield from rank_data(list(seq_or_iter),key)
        return
    data: Sequence[Rank_Data]
    if isinstance(seq_or_iter[0],Rank_Data):
        data = seq_or_iter
    else:
        empty_ranks: Tuple[float] = cast(Tuple[float],())
        data = list(
            Rank_Data(empty_ranks,raw_data)
            for raw_data in cast(Sequence[Source],seq_or_iter)
        )
    for r, rd in rerank(data,key):
        new_ranks = cast(
            Tuple[float],
            rd.rank_seq + cast(Tuple[float],(r,))
        )
        yield Rank_Data(new_ranks,rd.raw)
        )
