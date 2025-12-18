def check_even_or_Odd(number: int) -> str:
    if number % 2 == 0:
        return f"{number} is a Even number"
    else:
        return f"{number} is a Odd number"
print(check_even_or_Odd(10))
print(check_even_or_Odd(7)) 