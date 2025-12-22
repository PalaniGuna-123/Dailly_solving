def remove_duplicates(arr):
    result = []
    
    for x in arr:
        found = False
        
        for y in result:
            if x == y:
                found = True
        
        if not found:
            result.append(x)
    
    return result


nums = [1, 2, 2, 3, 4, 4, 5 ,54]
print(remove_duplicates(nums))

def remove_duplicate(arr):
    result =[]
    for x in arr:
        found = False
        for y in result:
            if x == y:
                found = True
        if not found:
            result.append(x)
    return result

nums=[11,11,2,33,44,55,5,55,5,5,67,77,8]
print(remove_duplicate(nums))



