def count_Vowels(S: str) -> int:
    vowels ="AEIOUaeiou"
    count=0
    for char in S:
        if char in vowels:
            count +=1
    return count
print(count_Vowels("Guna Vision"))