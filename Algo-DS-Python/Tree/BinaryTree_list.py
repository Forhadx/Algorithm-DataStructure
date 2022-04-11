
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # INSERT VALUE  
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return 'The binary tree is full'
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return f'{value} inserted'
    
    #SEARCH NODE   
    def searchNode(self, x):
        for i in range(len(self.customList)):
            if self.customList[i] == x:
                return True
        return False


    #   PRE-ORDER  TRAVERSAL :  root -> left -> right
    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index], end=' ')
        self.preOrder(index*2)
        self.preOrder(index*2 + 1)


    #   In-ORDER  TRAVERSAL :  left -> root -> right
    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrder(index*2)
        print(self.customList[index], end=' ')
        self.inOrder(index*2 + 1)

    # POST-ORDER  TRAVERSAL :  left -> right -> root
    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrder(index*2)
        self.postOrder(index*2 + 1)
        print(self.customList[index], end=' ')
    
    # LEVEL-ORDER
    def levelOrder(self, index):
        for i in range(index, self.lastUsedIndex):
            print(self.customList[i], end=' ')

    
    # DELETE-NODE
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'There is not any not to delete'
        for i in range(1, self.lastUsedIndex):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'Success'
        return 'Failed'
    
    # DELETE-BT
    def deleteBT(self):
        self.customList = None
        self.lastUsedIndex = 0
    

newBT =BinaryTree(10)
print(newBT.customList)


newBT.insertNode(1)
newBT.insertNode(2)
newBT.insertNode(3)
newBT.insertNode(4)
newBT.insertNode(5)
newBT.insertNode(6)
newBT.insertNode(7)
newBT.insertNode(8)
newBT.insertNode(9)

print(newBT.customList) # [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('search value 3: ',newBT.searchNode(3)) # True

print('preoder:- ')
newBT.preOrder(1) # 1 2 4 8 9 5 3 6 7

print('\ninOrder:- ')
newBT.inOrder(1) # 8 4 9 2 5 1 6 3 7

print('\npostOrder:- ')
newBT.postOrder(1) # 8 9 4 5 2 6 7 3 1

print('\nlevelOrder:- ')
newBT.levelOrder(1) # 1 2 3 4 5 6 7 8

print('\nafter delete node')
newBT.deleteNode(3)
print(newBT.customList) # [None, 1, 2, 9, 4, 5, 6, 7, 8, None]


newBT.deleteBT()