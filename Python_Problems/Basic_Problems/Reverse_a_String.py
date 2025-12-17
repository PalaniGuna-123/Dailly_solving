# Reverse a string problem write a function that returns the reverse of a given string.
# Example: input "hello" → output "olleh"

def reverse_string(S: str) -> str:
    return S[::-1]

print(reverse_string("Guna Vision"))


#  (s: str)

# s → parameter (input variable)

# : → type hint

# str → means s should be a string

# -> str :

# This is a return type hint

# It means the function will return a string value