def prompt(questions, retry=3):
    while retry >0:
        inp = input('{} ({})'.format(questions,retry))
        if inp == 'my secret':
            return True
        retry -=1
    return False
print(prompt("Type in your password"))
print(prompt("Type in your secret",1))

from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
