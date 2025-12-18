def sum_of_arr_elements(arr:list) -> int:
    total =0
    for num in arr:
        total += num
    return total

print(sum_of_arr_elements([1,2,3,4,5]))