# 2^0 + 2^1 + 2^2 + ... + 2^h = (2^(h+1)) - 1, total no of nodes in a complete binary tree
from queue import Queue

res = []
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.res = []

    # All defined here are DFS algorithms
    def inorder(self, root):
        if root is None:
            return
        self.preorder(root.left)
        res.append(root.data)
        self.preorder(root.right)
    def inorder_wr(self, root):
        if root is None:
            return
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.data)
            root = root.right
    def postorder(self, root):
        if root is None:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        res.append(root.data)
    def preorder(self, root):
        if root is None:
            return
        res.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    # All defined here are BFS algorithms
    def levelorder(self, root):
        if root is None:
            return
        queue = Queue()
        queue.put(root)
        curr = None
        while len(queue) > 0:
            curr = queue.get()
            self.res.append(curr.data)
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)
                