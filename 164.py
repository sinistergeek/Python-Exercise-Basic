def main():
    b = input("Number: ")
    a = input("Number: ")
    op = input("Operator (+-*/): ")

    command  = a + op +b
    print(command)
    res = eval(command)
    print(res)

main()
