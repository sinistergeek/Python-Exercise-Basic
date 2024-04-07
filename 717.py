from typing import Callable, Sequence, Dict, List, TypeVar
S_ = TypeVar("S_")
K_ = TypeVar("K_")
def group_by(
        key:Callable[[S_],K_],
        data: Sequence[S_]) -> Dict[K_,List[S_]]:
    def group_into(
            key: Callable[[S_],K_],
            collection: Sequence[S_],
            dictionary:Dict[K_,List[S_]]) -> Dict[K_,List[S_]]:
        if len(collection) == 0:
            return dictionary
        head,*tail = collection
        dictionary[Key(head).append(head)]
        return group_into(key, tail, dictionary)
    return group_into(key,data,defailtdict(list))
