import re
p1 = re.compile(r"(some) pattern")
p2 = re.compile(r"a (different) pattern")

from typing import Optional, Match
def matcher(text: str) -> Optional[Match[str]]:
    patterns = [p1,p2]
    matching = (p.search(text) for p in patterns)
    try:
        good = next(filter(None,matching))
        return good
    except StopIteration:
        pass
