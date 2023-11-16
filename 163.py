x = 3
answer = 'positive' if x > 0 else 'negative'
print(answer)

x = -3 
answer = 'positive' if x > 0 else 'negative'
print(answer)


def main():
    #length = 10
    #width = 3
    length = int(input('length: '))
    width = int(input('Width:'))

    if length <= 0:
        print("length is not positive")
        return
    if width <= 0:
        print("width is not positive")
        return
    area = length * width
    print("The area is ", area)

main()
