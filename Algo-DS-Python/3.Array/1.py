from  array import *

print('--------- Initialize Array ----------')
'''
    Initial Array:

        from array import *
        arrayName = array(typecode, [initializers])

        'i' - sign int - 2
        'f' - float - 4
        'd' - float - 8
        'u' - unicode char - 2
'''

arrInt = array('i', [1, 2, 3, 4])
print(arrInt) # array('i', [1, 2, 3, 4])

arrFloat = array('f', [1.2, 3.22, 5.23])
print(arrFloat) # array('f', [1.2000000476837158, 3.2200000286102295, 5.230000019073486])

arrStr = array('u', ['a', 'b', 'c'])
print(arrStr)   # array('u', 'abc')




print('----------------- apennd() ----------------')

arr3 = array('i', [1, 2, 3, 4])
arr3.append(6)
print(arr3) # array('i', [1, 2, 3, 4, 6])


print('-------------- insert in Array -------------')
'''
    array_name.insert(position, value)
'''

arr1 = array('i', [11, 22, 33, 44])

arr1.insert(0, 99)  
print('Insert in first', arr1)# array('i', [99, 11, 22, 33, 44]) 

arr1.insert(5, 88)  
print('Insert in last', arr1)# array('i', [99, 11, 22, 33, 44, 88])

arr1.insert(2, 66) 
print('Insert in middle', arr1)#  array('i', [99, 11, 66, 22, 33, 44, 88])

arr1.insert(20, 11111) 
print('Insert in out of size', arr1)# array('i', [99, 11, 66, 22, 33, 44, 88, 11111])
print(arr1[7]) # 11111 is place in position 7



print('-------------- Remove value in Array -------------')
'''
    array_name.remove(value)
'''

arr2 = array('i', [11, 22, 33, 44])

arr2.remove(33)
print(arr2) # array('i', [11, 22, 44])

# arr2.remove(100) # value isn't exist so give an error



print('----------------- pop() ----------------')

arr4 = array('i', [1, 2, 3, 4])
arr4.pop()
print(arr4) # array('i', [1, 2, 3])


print('----------------- reverse() ----------------')

arr = array('i', [1, 2, 3, 4])
arr.reverse()
print(arr) # array('i', [4, 3, 2, 1])


print('----------------- tolist() ----------------')
# convert array to list
arr = array('i', [1, 2, 3, 4])
print(arr.tolist()) # [1, 2, 3, 4]
