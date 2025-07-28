def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


# Example: Print first 10 Fibonacci numbers
fibonacci_series(10)
