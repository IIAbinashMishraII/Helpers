# PQ is an abstract data structure which can implemented using arrays, linked list, heap, BST
#             array     l.list      heap        BST
# enqueue      O(1)      O(n)      O(logn)     O(logn)
# dequeue      O(n)      O(1)      O(logn)     O(logn)
# peek         O(n)      O(1)      O(1)        O(1)

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
        new_node = PQNode(val, pr)
        if self.size == 0 or pr > self.head.pr:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.pr >= pr:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue underflow")
            return
        self.head = self.head.next
        self.size -= 1

    def peek(self):
        return self.head.data if self.size != 0 else "Queue is empty"


def test_llpq():
    llpq = LLPQ()
    llpq.enqueue(10, 2)
    llpq.enqueue(14, 4)
    llpq.enqueue(16, 4)
    llpq.enqueue(12, 3)
    print(llpq.peek())
    llpq.dequeue()
    print(llpq.peek())
    llpq.dequeue()
    print(llpq.peek())


class HPQ:
    def __init__(self) -> None:
        self.H = []
        self.size = 0

    # _methodName is a convention to name internal methods, that should be called outside the class
    def _swap(self, i, j):
        self.H[i], self.H[j] = self.H[j], self.H[i]

    def _shiftUp(self, i):
        # Basically for all elements in the array as long as the parent is smalled than child,
        # and if found small, it is swapped and run again with it's parent now.
        parent_index = (i - 1) // 2
        while i > 0 and self.H[parent_index] < self.H[i]:
            self._swap(parent_index, i)
            i = parent_index

    def _shiftDown(self, i):
        maxIndex = i
        left_child, right_child = (2 * i) + 1, (2 * i) + 2
        if left_child < self.size and self.H[left_child] > self.H[maxIndex]:
            maxIndex = left_child
        if right_child < self.size and self.H[right_child] > self.H[maxIndex]:
            maxIndex = right_child
        if i != maxIndex:
            self._swap(i, maxIndex)
            self._shiftDown(maxIndex)

    def enqueue(self, p):
        self.H.append(p)  # Add the new element at the end
        self.size += 1
        self._shiftUp(self.size - 1)  # Maintain heap property

    def dequeue(self):
        if self.size == 0:
            return "Heap is empty"
        max_value = self.H[0]
        self.H[0] = self.H[-1]
        self.H.pop()  # Remove the last element
        self.size -= 1
        if self.size > 0:
            self._shiftDown(0)
        return max_value

    def changePriority(self, i, p):
        oldp = self.H[i]
        self.H[i] = p
        if p > oldp:
            self._shiftUp(i)
        else:
            self._shiftDown(i)

    def peek(self):
        return self.H[0] if self.size > 0 else "Heap is empty"

    def remove(self, i):
        self.changePriority(i, float("inf"))  # Change priority to highest possible
        self.dequeue()  # Extract the element

    def display(self):
        print("Priority Queue:", self.H)


def test_hpq():
    pq = HPQ()
    pq.enqueue(45)
    pq.enqueue(20)
    pq.enqueue(14)
    pq.enqueue(12)
    pq.enqueue(31)
    pq.enqueue(7)
    pq.enqueue(11)
    pq.enqueue(13)
    pq.enqueue(7)

    pq.display()
    print("Node with maximum priority (peek):", pq.peek())
    print("Dequeued:", pq.dequeue())
    pq.display()

    pq.changePriority(2, 49)
    pq.display()

    pq.remove(3)
    pq.display()


test_lpq()
test_llpq()
test_hpq()
