from array import * 

print('------------ extend()-------------')
# extend array - join two array
arr1 = array('i', [1, 2, 3, 4])
arr2 = array('i', [11, 22, 33, 44])

arr1.extend(arr2)
print(arr1) # array('i', [1, 2, 3, 4, 11, 22, 33, 44])


print('------------ fromlist()-------------')
# fromlist array - join array with list
arr1 = array('i', [1, 2, 3, 4])
arr2 = [11, 22, 33, 44]

arr1.fromlist(arr2)
print(arr1) # array('i', [1, 2, 3, 4, 11, 22, 33, 44])


print('------------ index()-------------')
# find index by value of array- array_name(value)
arr1 = array('i', [11, 22, 33, 44, 55])

print(arr1.index(33))   # 2
# print(arr1.index(12))   # 12 is not here, give an error


print('------------ count()-------------')
arr = array('i', [1, 12, 3, 12, 12, 4])
print(arr.count(12)) # 3 , 12 has 3 time


print('------------ buffer_info()-------------')
# how to array  work - buffer_info() 
arr = array('i', [1, 2, 3, 4])
print(arr.buffer_info()) # (2194604507776, 4) = start_buffer, array_size


