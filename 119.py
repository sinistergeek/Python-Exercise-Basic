x = "The days of Python 2 are almost over. Python 3 is the king now."
if "z" in x or x.count("y") >= 2:
    print("True")

if type(x) is str and x.startswith("T"):
    print("True")
if x.index("t") < 10:
    print("True!")
else:
    print("False!")
