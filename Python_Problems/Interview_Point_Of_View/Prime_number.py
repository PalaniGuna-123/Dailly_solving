n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime Number")
else:
    # Assume the number is prime initially
    is_prime = True

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    # Print result
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

def PrimeNumber(n: int) -> int:
    n=int(input("Enter a number"))

    if n <=1:
        print("Not a Prime Number")
    else:
        is_Prime_Num= True
        
        for i in range(2,n):
            if n% i == 0:
                is_Prime_Num= False
                break
        if is_Prime_Num:
            print("this is a prime number")
        else:
            print(" This is Not a prime number")

PrimeNumber(3)
# iteration
# check divisibility from 2 to n-1  
# if divisible by any number in that range, it's not prime
# else it is prime          

#logic
# n=7
# i=2
# 7 % 2 !=0
# i=3
# 7 % 3 !=0
# i=4
# 7 % 4 !=0
# i=5               