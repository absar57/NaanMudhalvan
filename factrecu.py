def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = 5
result = factorial_iterative(number)
print(f"The factorial of {number} is: {result}")
