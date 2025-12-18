def cumulative_sum(arr: list) -> list:
    total=0
    result=[]

    for i in arr:
        total+=i
        result.append(total)
    return result

print(cumulative_sum([1,2,3,4]))

#output [1, 3, 6, 10]
