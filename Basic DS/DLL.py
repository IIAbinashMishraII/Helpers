from Helpers import DNode
# Remembet DLL is easier compared to LL because you can just do .prev and go back

class DLinkedList:
    def __init__(self):
        self.head = None 

    def insert_head(self, data):
        new_node = DNode(data)
        new_node.next = self.head # Pointing the new_node's next to the current head
        if self.head: # head is set, now to set prev pointer
            self.head.prev = new_node
        self.head = new_node # new head assigned
        return new_node

    def insert_tail(self, data):
        new_node = DNode(data)
        curr = self.head
        if self.head is None:
            self.head = new_node
            return new_node
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        return self.head

    def insert_index(self, data, index):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return 
        pos = 0
        curr = self.head
        while curr and pos+1 != index:
            curr = curr.next
            pos+=1
        if curr and curr.next:
            curr.next.prev = new_node
            new_node.next = curr.next
            new_node.prev = curr
            curr.next = new_node
        elif curr.next is None:
            self.insert_tail(new_node)
        else:
            print("Index out of bounds")

    def update_node(self, val, index):
        if self.head is None:
            print('Empty LL')
            return
        curr = self.head
        pos = 0
        if index == 0:
            self.head.data = val
            return
        while curr and pos+1 != index:
            curr = curr.next
            pos+=1
        curr.next.data = val

    def remove_head(self):
        if self.head is None or self.head.next is None:
            return 
        self.head = self.head.next
        self.head.prev = None

    def remove_tail(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next.prev = None
        curr.next = None
    
    def remove_index(self, index):
        if self.head is None:
            return 
        pos = 0
        curr = self.head
        while curr and pos+1 != index:
            curr = curr.next
            pos+=1
        if curr.next is None:
            self.remove_tail()
        elif curr is None:
            print("Index out of bounds")
        curr.next.prev = curr.prev
        curr.prev.next = curr.next

    def sizedll(self):
        count = 0
        curr = self.head
        while curr:
            count+=1
            curr = curr.next
        print(count)
    
    def printdll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print('None')



dll = DLinkedList()
dll.insert_head(6)
dll.insert_head(5)
dll.insert_head(7)
dll.insert_tail(1)
dll.insert_index(12, 2)
dll.update_node(77,2)
dll.printdll()
dll.remove_head()
dll.printdll()
dll.remove_tail()
dll.insert_head(51)
dll.insert_head(71)
dll.insert_tail(11)
dll.printdll()
dll.remove_index(3)
dll.printdll()
dll.sizedll()
