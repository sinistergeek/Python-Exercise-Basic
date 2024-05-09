from typing import Iterator
def local_gzip(pattern:str) -> Iterator[Iterator[str]]:
    zip_logs = glob.glob(pattern)
    for zip_file in zip_logs:
        with gzip.open(zip_file,"rb") as log:
            yield(line.decode('us-ascii').rstrip() for line in log)
