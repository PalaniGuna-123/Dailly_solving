text="PYthon programming"

# indexing
first_char = text[0]
last_char = text[-1]
last= text[-2]
print("First character:", first_char)
print("Last character:", last)

# slicing
substring = text[0:9]  # 'python'
print("Substring (0-6):", substring)

#negative indexing
neg_index_substring = text[-11:-1]  # 'python programmin'
print("Negative Index Substring (-11 to -1):", neg_index_substring)

#string reverse 

reversed_string = text[::-1]
print("Reversed String:", reversed_string)

#concatenation
greeting = "Hello, "
full_greeting = greeting + text
print("Concatenated String:", full_greeting)


# uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)

# lowercase
lower_text = text.lower()
print("Lowercase:", lower_text)

# capitalize
capitalized_text = text.capitalize()
print("Capitalized:", capitalized_text)

# replace
replaced_text = text.replace("PYthon", "Java")
print("Replaced Text:", replaced_text)

# find
index_of_programming = text.find("programming")
print("Index of 'programming':", index_of_programming)

# striding methods
# Extract every second character from the string
strided_string = text[::2]
print("Strided String (every 2nd char):", strided_string)