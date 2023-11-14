def my_func(x):
    my_new_list = []
    for i in x:
        if i > 4:
            my_new_list.append(i ** 2)
    return my_new_list
result = my_func((2,3,4,5,6,9))
print(result)
