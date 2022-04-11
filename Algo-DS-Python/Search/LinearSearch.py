
# Linear Search

def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return True
    return False

print(linearSearch([1, 2, 3, 4, 5], 4)) # True

print(linearSearch([1, 2, 3, 4, 5], 99))  # False

