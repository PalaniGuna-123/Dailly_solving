# Input: [10, 20, 5, 8]
# Output: 10

def find_second_largest(arr):
    first = second = float('-inf')
    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None  
# Example usage
numbers = [10, 20, 5, 8]
second_largest = find_second_largest(numbers)
print(f"The second largest element is: {second_largest}")