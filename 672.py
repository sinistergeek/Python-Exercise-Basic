mean=(sum float(pair[1]) for pair in sample_I) / len(sample_I)
)
for subset in sample_I, sample_II, sample_III, sample_III:
    mean = (sum(float(pair[1]) for pair in subset) / len(subset))
    print(mean)

from pathlib import Path
import json

username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")
