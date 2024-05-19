def calc_sum(sum_list):
    smallest_value = min(num_list)
    largest_value = max(num_list)
    total = smallest_value + largest_value
    return total
numbers=[5,6,3,8,9]
result = calc_sum(numbers)
print(result)
