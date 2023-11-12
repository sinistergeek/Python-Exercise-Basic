def calculate(number):
    i = 2
    factors = []
    while i*i <= number:
        if not number%i ==0:
            i+=1
        else:
            number = number//i
            factors.append(i)

        if number > 1:
            factors.append(number)
            print(factors)

            return factors


a = calculate(123)
print(a)
