from typing import TextIO 
import csv 
from collections import Counter 
from types import SimpleNamespace 

def defect_reduce(input_file: TextIO) -> Counter:
    rdr = csv.DictReader(input_file)
    assert set(rdr.fieldnames) == set(
        ["defect_type","serial_number","shift"])
    rows_ns = (simpleNamespace(**row) for row in rdr)
    defects = (
    (row.shift,row.defect_type)
    for row in rows_ns if row.defect_type 
    )
    tally = Counter(defects)
    return tally 
