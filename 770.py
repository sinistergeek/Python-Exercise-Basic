from typing import Iterator
def access_iter(
        source_iter: Iterator[Iterator[str]]
    ) -> Iterator[Access]:
    for log in source_iter:
        for line in log:
            match = format_pat.match(line)
            if match:
                yield Access(**match.groupdict())
