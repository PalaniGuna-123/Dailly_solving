def sum_of_numbers_divisible_by_3_and_5(number1: int , number2: int) -> int:
    sum=0
    for i in range(number1,number2 +1):
        if i % 3 == 0 and i % 5 == 0:
            sum +=i
    return sum

print(sum_of_numbers_divisible_by_3_and_5(3,90))
        