def sum_between_two_numbers(a: int,b: int) -> int:
    total =0
    for i in range(a,b+1): #Loop from a to b
        total +=i
    return total

print(sum_between_two_numbers(1,5))