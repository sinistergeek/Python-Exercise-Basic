def analysis(filename: str) -> Dict[str,int]:
    details = path_filter(
        access_detail_iter(
            access_iter(
                local_gzip(filename)
            )
        )
    )
    books = book_filter(details)
    totals = reduce_book_total(books)
    return totals
