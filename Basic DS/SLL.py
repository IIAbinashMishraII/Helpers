class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Pointer to the address of the next node in the memory

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_index(self, data, index):
        if index == 0:
            self.insert_head(data)
        curr = self.head
        pos = 0
        while curr and pos+1 != index:
            pos+=1
            curr=curr.next
        if curr != None:
            new_node = Node(data)
            new_node.next = curr.next 
            curr.next = new_node
        else:
            print('Index out of bounds')

    def insert_tail(self, val):
        curr = self.head
        new_node = Node(val)
        # Why do we need to use self.head instead of cuur here? 
        # Because if curr is empty, it will just be a local variable. It will not point to anything and will not work.
        # Else, it references the object self.head, doesn't hold it by itself, so a change in curr.next works.
        if self.head is None:
            self.head = new_node 
            return
        else:
            while curr.next:
                curr = curr.next
            curr.next = new_node
        
    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_tail(self):
        if self.head is None:
            return
        curr = self.head
        # This step is to check if only node exists, thereby avoiding a Attribute error
        if curr.next is None:
            curr = None
            return
        # Why are we checking next.next (2 ups)?
        # I mean how will you go to previous node and point to none if you are already at the last node 
        # For eg- 3 -> 5 -> 7 -> 9, if you check curr.next and you reach 9 to remove it, how to go to 7 to point it to None
        while curr!= None and curr.next.next!=None:
            curr = curr.next
        curr.next = None

    def remove_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.remove_head()
        curr = self.head
        pos = 0
        while curr and pos+1 != index:
            pos+=1
            curr=curr.next
        if curr != None and curr.next!=None:
            curr.next = curr.next.next
        else:
            print('Index out of bounds')

        # Where does the previous curr.next go ????????

    def remove_node(self, val):
        if self.head is None:
            return
        curr = self.head
        if curr.data == val:
            self.remove_head()
            return
        while curr and curr.next.data != val:
            curr = curr.next
        if curr:
            curr.next = curr.next.next
        else:
            return

    def update_node(self, val, index):
        curr = self.head
        pos = 0
        if index == pos:
            curr.data = val
            return
        while curr and pos+1 != index:
            pos+=1
            curr=curr.next
        if curr != None:
            curr.data = val
        else:
            print('Index out of bounds')

    def sizell(self):
        count = 0
        curr = self.head 
        # Why don't we just use the self.head in the while loop instead of curr ????
        # 
        # It will alter the structure of the linked list. 
        # For eg- if we do printll() and then sizell(), we will get the Linked list but size as 0, bcoz 
        # we are pointing to the end of the linked list 
        while curr:
            count+=1
            curr = curr.next
        print(count)
    
    def printll(self):
        curr = self.head
        # Same as sizell()
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print(None)
        
ll =LinkedList()
ll.remove_head()
ll.remove_tail()
ll.remove_node(5)
ll.remove_index(2)
ll.insert_head(6)
ll.insert_head(5)
ll.insert_head(7)
ll.insert_tail(6)
ll.insert_tail(10)
ll.insert_tail(3)
ll.insert_tail(9)
ll.printll()
ll.remove_node(6)
ll.insert_head(1)
ll.insert_head(8)
ll.insert_index(66, 4)
ll.insert_tail(2)
ll.remove_head()
ll.remove_tail()
ll.remove_index(2)
ll.remove_index(22)
ll.update_node(69,4)
ll.printll()
ll.sizell()
