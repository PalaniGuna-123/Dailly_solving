# Write a Python program to calculate the area of a rectangle given its length and width.
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width   
# print(f"The area of the rectangle is: {area}")

# Create a program that takes a user's name and age as input and prints a greeting message.
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello, {name}! You are {age} years old.")
# Write a program to check if a number is even or odd.
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")    


# Given a list of numbers, find the maximum and minimum values.
# numbers = [34, 12, 45, 2, 89, 5]
# max_value = max(numbers)
# min_value = min(numbers)
# print(f"Maximum value: {max_value}")
# print(f"Minimum value: {min_value}")


# Create a Python function to check if a given string is a palindrome.
# def is_palindrome(s: str) -> bool:
#     s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
#     return s == s[::-1]
# print(is_palindrome("Mada M"))
# print(is_palindrome("Hello"))

# Calculate the compound interest for a given principal amount, interest rate, and time period.
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate (in %): "))
# time = float(input("Enter the time period in years: "))
# compound_interest = principal * (1 + rate / 100) ** time - principal
# print(f"The compound interest is: {compound_interest}")
#explaination
# A = P (1 + r/n)^(nt) - P
# A = amount of money accumulated after n years, including interest.
# P = principal amount (the initial amount of money)
# r = annual interest rate (in decimal)
# n = number of times that interest is compounded per year
# t = time the money is invested for in years   


# Write a program that converts a given number of days into years, weeks, and days.
# toals_days = int(input("Enter the number of days: "))
# years = toals_days // 365
# weeks = (toals_days % 365) // 7
# days = (toals_days % 365) % 7   
# print(f"{toals_days} days is equal to {years} years, {weeks} weeks, and {days} days.")
# Given a list of integers, find the sum of all positive numbers.
# numbers = [-10, 15, -20, 25, 30, -5]
# positive_sum = sum(num for num in numbers if num > 0)
# print(f"The sum of all positive numbers is: {positive_sum}")

# Create a program that takes a sentence as input and counts the number of words in it.
# sentence = input("Enter a sentence: ")
# word_count = len(sentence.split())
# print(f"The number of words in the sentence is: {word_count}")
# Implement a program that swaps the values of two variables.
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
