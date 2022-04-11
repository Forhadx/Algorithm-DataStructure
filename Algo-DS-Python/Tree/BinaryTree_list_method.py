
customList= []

def insertNode(value):
    customList.append(value)

def searchNode(value):
    for i in range(len(customList)):
        if customList[i] == value:
            return True
    return False

#   PRE-ORDER  TRAVERSAL :  root -> left -> right
def preOrder(index):
    if index >= len(customList):
        return
    print(customList[index], end=' ')
    preOrder(index*2 + 1)
    preOrder(index*2 + 2)

#   In-ORDER  TRAVERSAL :  left -> root -> right
def inOrder( index):
    if index >= len(customList):
        return
    inOrder(index*2 + 1)
    print(customList[index], end=' ')
    inOrder(index*2 + 2)


# POST-ORDER  TRAVERSAL :  left -> right -> root
def postOrder( index):
    if index >= len(customList):
        return
    postOrder(index*2 + 1)
    postOrder(index*2 + 2)
    print(customList[index], end=' ')

# LEVEL-ORDER
def levelOrder(index):
    for i in range(len(customList)):
        print(customList[i], end=' ')

# DELETE-NODE
def deleteNode( value):
    if len(customList) <= 0:
        return 'There is not any not to delete'
    for i in range(len(customList)):
        if customList[i] == value:
            customList[i] = customList[len(customList)-1]
            customList.pop()
            return 'Success'
    return 'Failed'

# DELETE-BT
def deleteBT():
    customList.clear()


insertNode(1)
insertNode(2)
insertNode(3)
insertNode(4)
insertNode(5)
insertNode(6)
insertNode(7)
insertNode(8)
insertNode(9)

print(customList)

print('find 7: ',searchNode(7))
print('find 7: ',searchNode(12))

print('preoder:- ')
preOrder(0) # 1 2 4 8 9 5 3 6 7


print('\ninOrder:- ')
inOrder(0) # 8 4 9 2 5 1 6 3 7

print('\npostOrder:- ')
postOrder(0) # 8 9 4 5 2 6 7 3 1

print('\nlevelOrder:- ')
levelOrder(0) # 1 2 3 4 5 6 7 8

print('\nafter delete node:-')
deleteNode(3)
print(customList) # [1, 2, 9, 4, 5, 6, 7, 8]

print('delete BT:-')
deleteBT()
print(customList)