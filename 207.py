def prompt(questions, retry=3):
    while retry >0:
        inp = input('{} ({})'.format(questions,retry))
        if inp == 'my secret':
            return True
        retry -=1
    return False
print(prompt("Type in your password"))
print(prompt("Type in your secret",1))
