def ranker(
        sorted_iter: Iterator[Rank_Data],
        base: float,
        same_rank_seq: List[Rank_Data],
    key: Callable[[Rank_Data],K_]
    ) -> Iterator[Tuple[float,Rank_Data]]:
    try:
        value = next(sorted_iter)
    except StopIteration:
        dups = len(same_rank_seq)
        yield from yield_sequence(
            (base+1+base+dups)/2, iter(same_rank_seq)
        )
        return
    if key(value.raw) == key(same_rank_seq[0].raw):
        yield from ranker(
            sorted_iter,base,same_rank_seq+[value],key
        )
    else:
        dups = len(same_rank_seq)
        yield from yield_sequence(
            (base+1+base+dups)/2,iter(same_rank_seq)
        )
        yield from ranker(
            sorted_iter,base+dups,[value],key
        )
