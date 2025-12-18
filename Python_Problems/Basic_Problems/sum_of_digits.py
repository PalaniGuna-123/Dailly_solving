def sum_of_digits(number: int) -> int:
    total=0
    while number > 0:
        total = total + number % 10 # 1234 % 10 = 4  Last digit extract 0 + 4 = 4

        number = number // 10       # 1234 // 10 = 123 Remove last digit 1234 // 10 = 123

    return total

print(sum_of_digits(1234))  


# 🟢 Second iteration

# number = 123

# ✔ 123 % 10 = 3
# ✔ total = 4 + 3 = 7
# ✔ number = 123 // 10 = 12

# 🟢 Third iteration

# number = 12

# ✔ 12 % 10 = 2
# ✔ total = 7 + 2 = 9
# ✔ number = 12 // 10 = 1

# 🟢 Fourth iteration

# number = 1

# ✔ 1 % 10 = 1
# ✔ total = 9 + 1 = 10
# ✔ number = 1 // 10 = 0