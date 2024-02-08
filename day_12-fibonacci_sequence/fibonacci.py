def fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

# Example usage
num_terms = 10
fibonacci = fibonacci_sequence(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fibonacci)
