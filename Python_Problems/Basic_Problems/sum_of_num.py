def sum_of_numbers(number: int) -> int:
    total =0
    for i in range(1,number+1): #Loop from 1 to n
        total += i  #Add each number to total
    return total

print(sum_of_numbers(5)) 
        