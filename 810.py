from typing import TextIO
from collections import Counter
import csv
def defect_counts(source: TextIO) -> Counter:
    rdr = csv.DictReader(source)
    assert set(rdr.fieldnames) == set(
            ["defect_type","serial_number","shift"]
            )
    rows_ns = (SimpleNamespace(**row) for row in rdr)
    convert = map(
            lambda d: ((d.shift,d.defect_code),int(d.count)),rows_ns 
            )
    return Counter(dict(convert))
