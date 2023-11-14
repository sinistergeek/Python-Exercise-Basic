x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]

if x[2][2] < 6:
    print("True!")
elif x[1][0] == 5:
    print("False!")
else:
    print("Nonen!")


if x[0][-1] > 3:
    print("true")
elif x[1][-1] < 9:
    print("False!")
else:
    print("None!")

if len(x[0]) >= 5:
    print("True")
elif len(x[1]) == 4:
    print("False")
else:
    print("None")

if sum(x[0]) > sum(x[2]):
    print("True!")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None!")

if max(x[0]) - x[2][1] == x[0][0]:
    print("True")
elif len(x[0]) - len(x[1]) == x[2][0]:
    print("False")
elif sum(x[2])%2 == 0:
    print("Maybe")
else:
    print("None")
