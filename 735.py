def rerank(
        rank_data_iter: Iterable[Rank_Data],
        key: Callable[[Rank_Data], K_]
    ) -> Iterator[Tuple[float,Rank_Data]]:
    sorted_iter = iter(
        sorted(
            rank_data_iter,key=lambda obj: key(obj.raw)
        )
    )
    head = next(sorted_iter)
    yield from ranker(sorted_iter,0,[head],key)1
