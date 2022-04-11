
class Node:
    def __init__(self, value=None):
        self.value = value,
        self.next = None

class SingleLinklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    

linkedlist = SingleLinklist()

print([node.value for node in linkedlist])


# node1 = Node(1)
# node2 = Node(2)

# linkedlist.head = node1
# linkedlist.head.next = node2
# linkedlist.tail = node2
