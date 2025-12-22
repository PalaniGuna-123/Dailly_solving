# Count Occurrence of Each Character (no dict)

def char_count(s):
    result = []

    for ch in s:
        found = False
        for item in result:
            if item[0] == ch:
                item[1] += 1
                found = True
        if not found:
            result.append([ch, 1])

    return result

text = "banana"
print(char_count(text))
