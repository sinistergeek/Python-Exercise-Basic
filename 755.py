def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

    return lst
data_list = [15,16,6,8,5]
sorted_list = bubble_sort(data_list)
print(f"Sorted_list: {sorted_list}")
