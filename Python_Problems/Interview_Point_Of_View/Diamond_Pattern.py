def Diamond_Pattern(n: int) -> None:
    # upper part
    for i in range(1,n+1):
        print(" "*(n - i ) + "*" * (2 * i -1))
    #lower part
    for i in range(n-1,0,-1):
        print(" "*(n-i) + "*" *(2 * i -1))

Diamond_Pattern(5)


def Diamond_Pattern2(n: int) -> None:
    for i in range(1,n+1):
        print(" "*(n-i) + "*" * (2 * i -1))
    for j in range(n-1,0,-1):
        print(" " * (n -j) + "*" *(2 * j- 1))
    
Diamond_Pattern2(5)