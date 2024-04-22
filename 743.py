JT_ = TypeVar('JT_')
def join(
        t1: ITerable[JT_],
        t2: Iterable[JT_],
        where: Callable[[Tuple[JT_,JT_]],bool]
    ) -> Iterable[Tuple[JT_,JT_]]:
    return filter(where, product(t1,t2))
