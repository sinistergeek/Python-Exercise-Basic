def all_cases(input_string,flag):
    up_string = input_string.upper()
    low_string = input_string.lower()
    if flag:
        return up_string,low_string
    else:
        return (up_string,low_string)


def middle_char(input_string):
    return input_string[len(input_string) // 2:len(input_string) // 2 + 1]

up_string,low_string = all_cases('AbC',True)
tuple_uplow_strings = all_cases('AbC',False)
print(up_string,low_string,type(up_string))
print(tuple_uplow_strings,type(tuple_uplow_strings))
print(middle_char('Mushrooms Hunting'))
