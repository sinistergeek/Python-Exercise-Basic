def rank_xy(pairs: Sequence[Pair] -> Iterator[Ranked_XY]):
    return(
        Ranked_XY(
            r_x=r_x,r_y=rank_y_raw[0],raw=rank_y_raw[1])
        for r_x, rank_y_raw in rank(rank(rank_y(pairs), lambda r: r.raw.x)
        )
    )
