# Anagram
def are_anagrams_skill(t1, t2):
    # Check if two strings are anagrams of each other

    # Step 1: Check length
    if len(t1) != len(t2):
        return False

    # Step 2: Create frequency dictionary for first string
    freq = {}
    for char in t1:
        freq[char] = freq.get(char, 0) + 1

    # Step 3: Decrease frequency based on second string
    for char in t2:
        if char in freq:
            freq[char] -= 1
        else:
            return False

    # Step 4: Check if all frequencies are zero
    for count in freq.values():
        if count != 0:
            return False

    return True
# Anagram
t1 = "listen"
t2 = "silent"
result = are_anagrams_skill(t1, t2)
print(f"Are '{t1}' and '{t2}' anagrams? {result}")


def are_anagrams(s1, s2):

    # Step 1: Check length
    if len(s1) != len(s2):
        return False

    # Step 2: Loop through first string
    for ch in s1:

        count1 = 0
        count2 = 0

        # Count character in first string
        for c in s1:
            if c == ch:
                count1 += 1

        # Count character in second string
        for c in s2:
            if c == ch:
                count2 += 1

        # Step 3: Compare counts
        if count1 != count2:
            return False

    # Step 4: All characters matched
    return True


# Input
s1 = "silent"
s2 = "listen"

# Function call
print(are_anagrams(s1, s2))
