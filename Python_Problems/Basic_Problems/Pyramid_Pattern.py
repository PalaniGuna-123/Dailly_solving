#Pyramid_Pattern Problem

def Pyramid_Pattern(rows: int) -> None:
    for i in range(1,rows+1):
        spaces=rows-i
        stars = 2*i-1
        print(" " * spaces + "*" * stars)   

Pyramid_Pattern(6)    


