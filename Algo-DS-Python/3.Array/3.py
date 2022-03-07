# Two dimensional array

import numpy as  np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''


print('---------- insert()----------')
# insert row or column in the two dimensional array 
# np.insert(array_name, index, [values], axis= 0,1 ) // 0=row, 1=col

newArr = np.insert(arr, 2, [[10, 20, 30]], axis=1)
print('insert col: \n',newArr)
''''
insert col:
 [[ 1  2 10  3]
 [ 4  5 20  6]
 [ 7  8 30  9]]
'''

newArr = np.insert(arr, 2, [[10, 20, 30]], axis=0)  # if [[10, 20, 30, 40]] -> give an error
print('insert row: \n',newArr)
'''
insert row:
 [[ 1  2  3]
 [ 4  5  6]
 [10 20 30]
 [ 7  8  9]]
'''


print('---------- append()----------')
# append value in the last of row or col
# np.insert(array_name, [values], axis= 0,1 ) // 0=row, 1=col

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


newArr = np.append(arr,  [[10], [20], [30]], axis=1)  
print('insert row: \n',newArr)
'''
insert col:
 [[ 1  2  3 10]
 [ 4  5  6 20]
 [ 7  8  9 30]]
'''


newArr = np.append(arr, [[10, 20, 30]], axis=0)
print('insert row: \n',newArr)
''''
insert row:
 [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 20 30]]
'''

print('---------- delete()----------')
# delete row or col

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


newArr = np.delete(arr, 1, axis=1)
print('delete col: ',newArr)
'''
[[1 3]
 [4 6]
 [7 9]]
'''

newArr = np.delete(arr, 1, axis=0)
print('delete row: \n',newArr)
'''
 [[1 2 3]
 [7 8 9]]
'''