def create_counter(count=0):
    def internal():
        nonlocal count
        count += 1
        return count
    return internal
counter = create_counter()

print(counter())
print()


other = create_counter(42)
print(counter())
print(other())
print(counter())
print(other())
