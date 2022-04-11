'''
que: How to find the sum of digits of a positive 
    integer number using recursion?
'''

def sumOfDigit(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sumOfDigit(n//10)

print(sumOfDigit(223))   # 2 + 2 + 3 = 7
