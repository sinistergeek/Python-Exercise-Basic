from contextlib import ExitStack
import csv

def row_iter_csv_tab(*filenames: str) -> Iterator[List[str]]:
    with ExitStack() as stack:
        files = [
            stack.enter_context(cast(TextIO,open(name,'r')))
            for name in filenames
        ] # types: List[TextIO]
        readers = map(
            lambda f: csv.reader(f, delimiter='\t'),files
        )
        yield from chain(*readers)
