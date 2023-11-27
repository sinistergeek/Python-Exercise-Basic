counter = 0
dot_counter = ''

def update_counter():
    global counter,dot_counter
    counter += 1
    dot_counter += '.'

[update_counter() for _ in range(40)]
print(counter)
print(dot_counter)
