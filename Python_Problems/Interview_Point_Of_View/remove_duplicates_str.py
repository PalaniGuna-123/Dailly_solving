def remove_duplicate_str(s):
    result = []

    for x in s:
        found = False

        for y in result:
            if x == y:
                found = True

        if not found:
            result.append(x)

    # convert list back to string
    final_str = ""
    for ch in result:
        final_str = final_str + ch

    return final_str


text = "mississippyi"
print(remove_duplicate_str(text))
