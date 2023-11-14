x = [115,115.9,116.01,["length","width","height"],109,115,119.5,["length","width","height"]]
if len(x) >= 8 and type(x[6]) is float:
    print("True!")
else:
    print("False!")

if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("True!")

else:
    print("False!")

if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print("True!")
else:
    print("False!")


