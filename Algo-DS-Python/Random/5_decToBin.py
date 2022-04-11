'''
que: decimal to binary number

'''

def decimalToBinary(n):
    if n== 0:
        return 0
    else:
        return decimalToBinary(int(n/2)) * 10 + + (n%2)                       


print(decimalToBinary(13)) #1101


print(""" Binary & Decimal conversation """)

print(bin(5)) # 0b101, D->B , 0b define binary number start

print(int('0b101', 2)) # 5, 2 is binary base value