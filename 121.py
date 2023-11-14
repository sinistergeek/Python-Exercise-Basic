x =  {1:"Python",2:"Java",3:"Javascript",4:"Ruby",5:"Perl",6:"C#",7:"C++"}

if x[5] == "Perl" or len(x) % 5 < 2:
    print("True!")
else:
    print("False!")


if sorted(x.values())[-1][-1] == "n":
    print("True!")
else:
    print("False!")
