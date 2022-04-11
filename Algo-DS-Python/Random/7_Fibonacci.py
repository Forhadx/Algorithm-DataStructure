# fibonacci:  0 1 1 2 3 5

def fibonacci(n):
    if n >=0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) # at position 4 value is 3
