# Binary Search

import math

def binarySearch(arr, val):
    arr.sort()
    # print(arr)
    start = 0
    end = len(arr) - 1

    while start < end:
        middle = math.floor((start+end)/2)

        if arr[middle] == val:
            print('Find in index', middle)
            return
        
        if arr[middle] < val:
            start = middle + 1
        
        if arr[middle] > val:
            end = middle -1
    


binarySearch([11, 25, 3, 34, 9], 25)