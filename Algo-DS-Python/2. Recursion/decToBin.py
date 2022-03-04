'''
que: decimal to binary number

'''

def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer'
    if n== 0:
        return 0
    else:
        return decimalToBinary(int(n/2)) * 10 + + (n%2)                       


print(decimalToBinary(13)) #1101
