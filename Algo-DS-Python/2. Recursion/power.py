'''
que: Calculate power of a number using recursion?

'''

def powerOfNum(x, n):
    assert n>=0 and int(n) == n, 'number must be positive integer'
    if n == 0:
        return 1
    return x * powerOfNum(x, n -1)

print(powerOfNum(2, 4)) # 2*2*2*2 = 16

print(powerOfNum(3.2, 4)) # 104.85760000000003
