def find_max_min(arr):
    # Step 1: Initialize max and min as the first element
    maximum = arr[0]
    minimum = arr[0]
    

    # Step 2: Loop through the list
    for num in arr:
        # Check for maximum
        if num > maximum:
            maximum = num
        
        # Check for minimum
        if num < minimum:
            minimum = num

    return maximum, minimum

# Example usage
numbers = [11, 33, 5, 44, 22, 55]
max_num, min_num = find_max_min(numbers)
print("Maximum:", max_num)
print("Minimum:", min_num)
