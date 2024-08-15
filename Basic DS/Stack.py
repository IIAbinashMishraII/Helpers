# Stack implementation using Linked List and List.

# Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ll_stack:
    def __init__(self, n):
        self.head = None
        self.n = n
        self.size = 0

    def push(self, data):
        if self.size >= self.n:
            print('Stack overflow')
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size <= 0:
            print('Stack underflow')
            return
        popped = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.n
    
    def top(self):
        if self.head is None:
            return 'Stack is Empty'
        return self.head.data

    def printstack(self):
        curr = self.head
        while curr:
            print(curr.data, end=' <- ')
            curr = curr.next
        print('bottom')

def lls_test():
    lls = ll_stack(int(input("lls_test:")))
    lls.pop()
    lls.push(5)
    lls.push(6)
    lls.push(7)
    lls.push(8)
    lls.printstack()
    lls.pop()
    print(lls.isEmpty())
    print(lls.isFull())
    print(lls.top())
    lls.push(9)
    lls.push(1)
    lls.push(3)
    lls.printstack()
    print(lls.isEmpty())
    print(lls.isFull())
    lls.printstack()
    lls.pop()
    lls.printstack()



# List implementation
class list_stack:
    def __init__(self, n):
        self.a = []
        self.size = 0
        self.n = n
    def push(self, data):
        if self.size >= self.n:
            print('Stack overflow')
            return
        self.a.append(data)
        self.size += 1
    def pop(self):
        if self.size <= 0:
            print('Stack underflow')
            return
        self.a.pop()
        self.size -= 1
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    def isFull(self):
        if self.size == self.n:
            return True
        return False
    def top(self):
        return self.a[self.size - 1]
    def printstack(self):
        print('bottom', end =' -> ')
        for i in self.a:
            print(i, end =' -> ')
        print('top')

def ls_test():
    ls = list_stack(int(input("ls_test:")))
    ls.pop()
    ls.push(5)
    ls.push(6)
    ls.push(7)
    ls.push(8)
    ls.printstack()
    ls.pop()
    print(ls.isEmpty())
    print(ls.isFull())
    print(ls.top())
    ls.push(9)
    ls.push(1)
    ls.push(3)
    ls.printstack()
    print(ls.isEmpty())
    print(ls.isFull())
    ls.printstack()
    ls.pop()
    ls.printstack()

lls_test()
ls_test()