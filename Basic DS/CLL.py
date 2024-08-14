# Went further today

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Pointer to the address of the next node in the memory

class CLinkedList:
    def __init__(self):
        self.head = None 

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
    
    def insert_index(self, data, index):
        new_node = Node(data)
        if index<0:
            print('Invalid index')
            return
        elif index==0:
            self.insert_head(data)
            return
        pos = 0
        curr = self.head
        while curr.next != self.head and pos+1 != index:
            curr = curr.next
            pos+=1
        if curr is None:
            print('Invalid index')
        new_node.next = curr.next
        curr.next = new_node
        
    def update_node(self, val, index):
        if self.head is None:
            print('Empty LL')
            return
        curr = self.head
        pos = 0
        if index == 0:
            self.head.data = val
            return
        while curr.next!=self.head and pos+1 != index:
            curr = curr.next
            pos+=1
        curr.next.data = val

    def remove_head(self):
        if self.head is None:
            print('Empty LL')
            return
        self.head = self.head.next

    def remove_tail(self):
        if self.head is None:
            print('Empty LL')
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        curr.next = self.head

    def remove_index(self, index):
        if self.head is None:
            print('Empty LL')
            return
        if index == 0:
            self.remove_head()
            return 
        curr = self.head
        pos = 0
        while curr.next != self.head and pos+1 != index:
            curr = curr.next
            pos += 1
        if curr.next == self.head:
            print('Invalid Index')
        curr.next = curr.next.next

    def printcll(self):
        if not self.head:
            return 
        curr = self.head
        # Same as sizell()
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
            if curr == self.head:
                break
        print('...cont')

    def sizecll(self):
        if self.head is None:
            print(0)
            return 
        count = 1
        curr = self.head.next
        # Why don't we just use the self.head in the while loop instead of curr ????
        # 
        # It will alter the structure of the linked list. 
        # For eg- if we do printll() and then sizell(), we will get the Linked list but size as 0, bcoz 
        # we are pointing to the end of the linked list 
        while curr != self.head:
            count+=1
            curr = curr.next
        print(count)
        
cll =CLinkedList()
# cll.remove_head()
# cll.remove_tail()
# cll.remove_node(5)
# cll.remove_index(2)
cll.insert_head(6)
cll.insert_head(5)
cll.insert_head(7)
cll.insert_tail(6)
cll.insert_tail(10)
cll.insert_tail(3)
cll.insert_tail(9)
cll.printcll()
# cll.remove_node(6)
cll.insert_head(1)
cll.insert_head(8)
cll.insert_index(66, 4)
cll.insert_tail(2)
cll.remove_head()
cll.remove_tail()
cll.remove_index(2)
# cll.remove_index(22)
cll.update_node(69,4)
cll.printcll()
cll.sizecll()
