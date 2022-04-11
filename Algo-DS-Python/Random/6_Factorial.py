#  factorial


def factorial(n):
    # print(n)
    if n <= 1:
        return 1
    return n * factorial(n-1)

x = factorial(4)

print(x) # 24

