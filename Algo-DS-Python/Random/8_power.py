'''
que: Calculate power of a number using recursion?

'''

from math import ceil


def powerOfNum(x, n):
    if n == 0:
        return 1
    return x * powerOfNum(x, n -1)

print(powerOfNum(2, 4)) # 2*2*2*2 = 16

print(powerOfNum(3.2, 4)) # 104.85760000000003


print(pow(2,3))

print(ceil(22/3))