'''
def factorial(n):
    print(n)
    if n <= 1:
        return 1
    return n * factorial(n-1)

x = factorial(4)
print(x)

'''

# from mimetypes import init


def factorial(n):
    assert n >= 0 and int(n) == n, 'Number must be positive integer'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 24

print(factorial(-1)) # -1, 1.1 its send an error msg
