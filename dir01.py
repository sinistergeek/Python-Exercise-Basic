file_handle = open("demo.txt","r+")
try:
    print(file_handle.read())
finally:
    file_handle.close()
