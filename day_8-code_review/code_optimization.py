def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result

# Example usage
n = 10
result = sum_of_squares(n)
print(f"The sum of squares from 1 to {n} is: {result}")

def sum_of_squares_optimized(n):
    return sum(i**2 for i in range(1, n+1))

# Example usage
n = 10
result = sum_of_squares_optimized(n)
print(f"The sum of squares from 1 to {n} is: {result}")
