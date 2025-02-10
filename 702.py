from typing import Callable, Iterable, Tuple, Iterator, Any

Conv_F = Callable[[float],float]
Leg = Tuple[Any, Any, float]

def convert(
        conversion: Conv_f,
        trip: Iterable[Leg]) -> Iterator[float]:
    return(
            conversion(distance) for start, end, distance in trip
        )

from pathlib import Path
import json

username = input("What is your name?")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"we'll remember you whenn you come back, {username}!")
