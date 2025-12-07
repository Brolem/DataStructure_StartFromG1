'''二叉搜索树的实现(Binary Search Tree Implementation)'''

class BstNode:
    def __init__(self, data): #封装了BstNode创建方法
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None #指向根节点的指针

    def insert(self, data):
        if not self.root:
            self.root = BstNode(data) #创建根节点
        else:
            self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BstNode(data)
            else:
                self._insert_rec(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = BstNode(data)
            else:
                self._insert_rec(node.right, data)
    
    # Alternative insert method 传入的root是局部变量           
    def Insert(self, root, data):
        if root is None:
            return BstNode(data)
        if data < root.data:
            root.left = self.Insert(root.left, data)
        elif data > root.data:
            root.right = self.Insert(root.right, data)
        return root

    def search(self, data):
        return self._search_rec(self.root, data)

    def _search_rec(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_rec(node.left, data)
        return self._search_rec(node.right, data)
    
    # Alternative search method
    def Search(self, root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self.Search(root.left, data)
        return self.Search(root.right, data)
    
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    number = int(input("Enter a number to search: "))
    result = bst.search(number)
    if result: print("Found")
    else: print("Not found")