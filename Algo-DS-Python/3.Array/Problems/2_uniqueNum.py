# Check if all list value is unique

myList = [1, 2, 3, 5, 2, 6]

def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True


print(isUnique(myList))