def count_Vowels(S: str) -> int:
    vowels ="AEIOUaeiou"
    count=0
    for char in S:
        if char in vowels:
            count +=1
    return count
print(count_Vowels("Guna Vision"))

def count_Vowels_with_letter(S: str) -> str:
    vowels ="AEIOUaeiou"
    Str=""
    for char in S:
        if char in vowels:
            Str +=char
    return Str + " : " + str(len(Str))

print(count_Vowels_with_letter("Guna Vision"))
