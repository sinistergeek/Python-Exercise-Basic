student = {
        "name":"Andy",
        "id":"0026"
        }
print(student.get("id"))

class Student:
    name = "Andy"
    id = "0026"
print(getattr(Student,'id'))

os.chdir("c:\\mydir")
cwd = os.getcwd()
print("The current working directory is:",cwd)
