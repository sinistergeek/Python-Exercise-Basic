from typing import Callable, Tuple, List, TypeVar, cast, Dict
D_ = TypeVar("D_")
K_ = TypeVar("K_")
def rank(
        data: Iterable[D_],
        key: Callable[[D_],K_]= lambda obj: cast(k,obj)
        ) -> Iterator[Tuple[float,D_]]:

    def build_duplicates(
            duplicates:Dict[K_,List[D_]],
            data_iter: Iterator[D_],
            key: Callable[[D_],K_]
            ) -> Dict[k,List[D_]]:
        for item in data_iter:
            duplicates[key(item)].append(item)
        return duplicates

    def rank_output(
            duplicates: Dict[K_,List[D_]].
            key_iter: Iterator[K_],
            base: int=0
            ) -> Iterator[Tuple[float,D_]]:
        for k in key_iter:
            dups = len(duplicates[k])
            for value in duplicates[k]:
                yield(base+1+base+dups)/2,value
            base += dups

    duplicates = build_duplicates(
            defaultdict(list),iter(data),key)
    return rank_output(duplicates, iter(sorted(duplicates)),0)
