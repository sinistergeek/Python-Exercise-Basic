with open("myfile.txt","r") as f:
    chunk = 1024
    contents = ""
    while True:
        data = f.read(chunk)
        if not data:
            break
        contents += data
        print(contents)
