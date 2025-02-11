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


from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back,{username}!")

else:
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
