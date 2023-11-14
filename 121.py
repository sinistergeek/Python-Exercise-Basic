x =  {1:"Python",2:"Java",3:"Javascript",4:"Ruby",5:"Perl",6:"C#",7:"C++"}

if x[5] == "Perl" or len(x) % 5 < 2:
    print("True!")
else:
    print("False!")


if sorted(x.values())[-1][-1] == "n":
    print("True!")
else:
    print("False!")

if sorted(x.keys())[-1] % sorted(x.keys())[-2]==sorted(x.keys())[0]:
    print("True!")
else:
    print("False!")

if sum(x) < len(x[1]+x[2]+x[3]+x[4]+x[5]):
    print("True!")
else:
    print("False!")


