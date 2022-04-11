

# Find missing number
'''
    li = [1, 2, 3, 5]
    what will be missing in serial of this array
    
    1 to 5 addition = 1+2+3+4+5 = 15
    li values addition = 1+2+3+5 = 11

    missing number = 15 - 11
'''


myList = [1, 2, 3, 5]

def missingNumber(li, n):
    sum_1 = n*(n+1)/2
    sum_2 = sum(li)

    miss = sum_1 - sum_2
    print('Missing number: ',miss)

missingNumber(myList, 5)