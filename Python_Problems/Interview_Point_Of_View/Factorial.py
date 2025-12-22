def factorial(n):
    # Step 1: Handle 0 or negative numbers
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    # Step 2: Initialize result
    result = 1

    # Step 3: Loop from 1 to n
    for i in range(1, n + 1):
        result = result * i  # Multiply result by current number

    return result

# Example usage
num = 5
print("Factorial of", num, "is", factorial(num))
