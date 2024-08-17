from Helpers import DNode, SNode
# Stack implementation using Linked List and List. Basically, stack is just a list with extra care.
# Queue implementation using Linked List and Stack
# Deque implementation using Doubly Linked List
# Queues can be implemtented using list, collections.deque (double ended queue), queue.Queue

# Stack Linked List implementation
class ll_stack:
    def __init__(self, n):
        self.head = None
        self.n = n
        self.size = 0

    def push(self, data):
        if self.size >= self.n:
            print('Stack overflow')
            return
        new_node = SNode(data)
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

# Stack List implementation
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

# Queue Linked List implementation
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.tail is None and self.head is None
            
    def enqueue(self, data):
        new_node = SNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.head is None:
             print('Queue is empty')
             return 
        self.head = self.head.next
        if self.head is None:
            self.tail = None
    
    def front(self):
        if self.is_empty():
             print('Queue is empty')
             return 
        print("front: ", self.head.data)
        return
    
    def rear(self):
        if self.is_empty():
             print('Queue is empty')
             return 
        
        print("rear: ", self.tail.data)
        return
def llq_test():
    llq = Queue()
    llq.enqueue(5)
    llq.enqueue(4)
    llq.enqueue(2)
    llq.enqueue(11)
    llq.front()
    llq.rear()
    llq.dequeue()
    llq.dequeue()
    llq.enqueue(9)
    llq.front()
    llq.rear()

lls_test()
ls_test()
llq_test()