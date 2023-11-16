a_in = input("Enter second the number")
b_in = input("Enter second number")

choice =input("Enter the 1 = Ascii or 2 = len")

if choice == '1':
    first = a_in > b_in
    second = a_in < b_in
elif choice =='2':
    first = len(a_in) > len(b_in)
    second = len(a_in)<len(b_in)

if first:
    print("fist is bigger")
elif second:
    print("second is bggier")
else:
    print("equal")
