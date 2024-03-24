def numbers():
    for i in range(1024):
        print(f"= {i}")
        yield i
