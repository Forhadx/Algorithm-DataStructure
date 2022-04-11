'''
    ----- bitwise ------

    and         &       x & y
    or          |       x | y
    not         ~       ~x
    xor         ^       x^y
    rightshift  >>      x>>
    leftshift   <<      x<<

'''


a = 10
b = 4

# AND
print('a & b =', a & b) # 0

# OR
print('a | b =', a | b) # 14

# NOT
print('~a = ', ~a)  # -11

# XOR
print('a ^ b = ', a ^ b) # 14

# LEFT-SHIFT
print('a >> 1 = ', a >> 1) # 5
print('a >> 2 = ', a >> 2) # 2

# RIGHT-SHIFT
print('a << 1 = ', a << 1) # 20
print('a << 2 = ', a << 2) # 40



'''
a = 10 = 1010
b = 4 = 0100

AND:    a & b = 1010 & 0100 = 0000 = 0

OR:    a | b = 1010 | 0100 = 1110 = 14

NOT:    ~a = ~1010 = = -(1010 + 1) = -11

XOR:    a ^ b = 1010 ^ 0100 = 1110 = 14

LEFTSHIFT: a >> 1 = 0000 0101 = 5

RIGHTSHIFT: b << 2 = 1101 1000 = -40 


'''