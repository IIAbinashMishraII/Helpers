# PQ is an abstract data structure which can implemented using arrays, linked list, heap, BST
#             array     l.list      heap        BST
# enqueue      O(1)
# dequeue      O(n)
# peek         O(n)

import sys


# Array PQ implementation
class item:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class LPQ:
    def __init__(self) -> None:
        self.queue = []
        self.size = 0

    def enqueue(self, val, priority):
        self.size += 1
        self.queue.append(item(val, priority))

    def peek(self):
        if self.size == 0:
            return None
        highestPriority = -sys.maxsize
        ind = -1
        for i in range(self.size):
            if self.queue[i].priority > highestPriority or (
                self.queue[i].priority == highestPriority
                and self.queue[i].val > self.queue[ind].val
            ):
                highestPriority = self.queue[i].priority
                ind = i
        return ind

    def dequeue(self):
        ind = self.peek()
        if ind is not None:
            self.queue.pop(ind)
            self.size -= 1


def test_lpq():
    lpq = LPQ()
    lpq.enqueue(10, 2)
    lpq.enqueue(14, 4)
    lpq.enqueue(16, 4)
    lpq.enqueue(12, 3)
    print(lpq.queue[lpq.peek()].val)
    lpq.dequeue()
    print(lpq.queue[lpq.peek()].val)
    lpq.dequeue()
    print(lpq.queue[lpq.peek()].val)


class PQNode:
    def __init__(self, data, pr) -> None:
        self.next = None
        self.data = data
        self.pr = pr


class LLPQ:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def enqueue(self, val, pr):
        if self.size == 0:
            self.head = PQNode(val, pr)
            return
        curr = self.head
        new_node = PQNode(val, pr)
        if curr.pr < new_node.pr:
            new_node.next = self.head
            new_node = self.head
            return
        while curr.next:
            if curr.next.pr <= new_node.pr:
                break
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
    
    def dequ

test_lpq()
