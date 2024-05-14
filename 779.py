from collections.abc import ItemsView
from typing import Iterable,Iterator
def book_filter(
        access_details_iter: Iterable[AccessDetails]
    ) -> Iterator[AccessDetails]
        def book_in_path(detail: AccessDetails) -> bool:
            path = tuple(
        item 
        for item in detail.url.path.split('/')
        if item 
    )
    return path[0] == 'book' and len(path) > 1
return filter(book_in_path,access_details_iter)
