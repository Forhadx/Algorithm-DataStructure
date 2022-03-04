def fibonacci(n):
    assert n >= 0 and int(n) == n , "should be positive interger num"
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) # at position 4 value is 3

print(fibonacci(-1)) # -1, 1.1 its give an error