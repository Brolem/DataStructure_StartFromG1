'''查找BST最大最小值及二叉树的高度'''

class BstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.BSTroot = None
    
    def insert(self, root, data):
        if root is None:
            return BstNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root
    
    def find_min(self, root):
        if root is None:
            print("Error: Tree is empty")
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    # 递归版
    def find_min_rec(self, root):
        if root is None:
            print("Error: Tree is empty")
            return -1
        if root.left is None:
            return root
        return self.find_min_rec(root.left)
    
    def find_max(self, root):
        if root is None:
            print("Error: Tree is empty")
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current
    
    def find_height(self, root):
        if root is None:
            return -1
        left_height =self.find_height(root.left)
        right_height = self.find_height(root.right)
        return max(left_height, right_height) + 1
    
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.BSTroot = bst.insert(bst.BSTroot, 10)
    bst.BSTroot = bst.insert(bst.BSTroot, 5)
    bst.BSTroot = bst.insert(bst.BSTroot, 15)
    bst.BSTroot = bst.insert(bst.BSTroot, 3)
    
    result1 = bst.find_min(bst.BSTroot)
    if result1 != -1:
        print(f"Minimum value: {result1.data}")
    result2 = bst.find_max(bst.BSTroot)
    if result2 != -1:
        print(f"Maximum value: {result2.data}")
        
    height = bst.find_height(bst.BSTroot)
    print(f"Height of the tree: {height}")