# Remembet DLL is easier compared to LL because you can just do .prev and go back

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next # Pointer to the address of the next node in the memory
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None 

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head # Pointing the new_node's next to the current head
        if self.head: # head is set, now to set prev pointer
            self.head.prev = new_node
        self.head = new_node # new head assigned
        return new_node

    def insert_tail(self, data):
        new_node = Node(data)
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
        pass

    def remove_head():
        pass

    def remove_tail():
        pass

    def remove_index():
        pass

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
dll.printdll()
dll.sizedll()
