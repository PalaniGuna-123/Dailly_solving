# Anagram

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
