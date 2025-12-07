'''二叉树的前序、中序、后序遍历'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        
        return node
    
    def pre_order(self, node):
        if node is None: return
        
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)
        
    def in_order(self, node):
        if node is None: return
        
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)
        
    def post_order(self, node):
        if node is None: return
        
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=' ')