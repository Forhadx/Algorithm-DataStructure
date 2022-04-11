
# Make custom stack

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # Push
    def push(self, value):
        if self.isFull():
            print(f'{value}, stack is full ')
            return 
        else:
            self.list.append(value)
            print(f'{value} inserted')
            return 
        
    # Pop
    def pop(self):
        if self.isEmpty():
            print('Stack is empty!')
            return
        else:
            print('list: ',self.list)
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return'Stack is empty'
        return self.list[len(self.list)-1]
    
    # delete stack
    def delete(self):
        self.list = None

s = Stack(4)

s.push(8)
s.push(2)
s.push(3)
s.push(5)
s.push(7)

print('---stack values---')
print(s)

s.pop()

print('---after pop---')
print(s)

print('peek value: ',s.peek())