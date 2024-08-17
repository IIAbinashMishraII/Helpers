class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None # Pointer to the address of the next node in the memory

class DNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next # Pointer to the address of the next node in the memory
        self.prev = prev