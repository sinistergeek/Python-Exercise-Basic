def my_func(x):
    my_new_list = []
    for i in range(5):
        my_new_list.append(i*x)
    return my_new_list
result = my_func(2)
print(result)
