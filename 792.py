def find_majority_element(num_list):

    for num in num_list:
        count = num_list.count(num)
        if count // 2:
            return num


numbers = [1,7,8,7,7,7]
result = find_majority_element(numbers)
print(result)
