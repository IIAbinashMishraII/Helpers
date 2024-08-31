# 2^0 + 2^1 + 2^2 + ... + 2^h = (2^(h+1)) - 1, total no of nodes in a complete binary tree
from queue import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class TreeAlgo:
    # All defined here are DFS algorithms
    def __init__(self) -> None:
        self.res = []
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.res.append(root.data)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.res.append(root.data)

    def preorder(self, root):
        if root is None:
            return
        self.res.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder_wr(self, root):
        self.res = []
        if root is None:
            return
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            self.res.append(curr.data)
            curr = curr.right
    
    def postorder_wr(self, root):
        self.res = []
        if root is None:
            return
        stack = []
        last_node_visited = None
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_node_visited != peek_node.right:
                    current = peek_node.right
                else:
                    self.res.append(peek_node.data)
                    last_node_visited = stack.pop()
    
    def preorder_wr(self, root):
        self.res = []
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            self.res.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # All defined here are BFS algorithms
    def levelorder(self, root):
        self.res = []
        if root is None:
            print('None')
            return
        queue = Queue()
        queue.put(root)
        curr = None
        while not queue.empty():
            curr = queue.get()
            self.res.append(curr.data)
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)
        
    def size_and_reverse_levelorder(self, root):
        self.res = []
        if root is None: 
            return
        queue = Queue()
        queue.put(root)
        curr = None
        size = 0
        while not queue.empty():
            curr = queue.get()
            size += 1
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)
            self.res.append(curr.data)
        return size, self.res[::-1]
        
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def clear(self):
        self.res = []

def test_tree():
    tree_algo = TreeAlgo()
    root = TreeNode(1)
    tree_algo.insert(root, 10)
    tree_algo.insert(root, 5)
    tree_algo.insert(root, 15)
    tree_algo.insert(root, 3)
    
    # Perform traversals
    tree_algo.inorder(root)
    print("Inorder traversal (recursive):", tree_algo.res)
    tree_algo.clear()
    tree_algo.inorder_wr(root)
    print("Inorder traversal (iterative):", tree_algo.res)
    tree_algo.clear()
    tree_algo.preorder(root)
    print("Preorder traversal (recursive):", tree_algo.res)
    tree_algo.clear()
    tree_algo.preorder_wr(root)
    print("Preorder traversal (iterative):", tree_algo.res)
    tree_algo.clear()
    tree_algo.postorder(root)
    print("Postorder traversal (recursive):", tree_algo.res)
    tree_algo.clear()
    tree_algo.postorder_wr(root)
    print("Postorder traversal (iterative):", tree_algo.res)
    tree_algo.clear()
    tree_algo.levelorder(root)
    print("Level order traversal:", tree_algo.res)
    size, reverse_levelorder = tree_algo.size_and_reverse_levelorder(root)
    print("Size of tree:", size)
    print("Reverse Level order traversal:", reverse_levelorder)
    height = tree_algo.height(root)
    print("Height of tree:", height)

test_tree()