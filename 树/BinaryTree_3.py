'''二叉树的层次遍历 使用队列：父节点出队，子节点入队(Lever Order Traversal)'''
import 队列.Queue_2 as queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None: return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
            
        return node
    
    def lever_order(self, node):
        if node is None: return
        q = queue.Queue()
        q.enqueue(node)
        
        while not q.is_empty():
            current = Node(q.front)
            print(current.data, end=' ')
            if current.left is not None:
                q.enqueue(current.left)
            if current.right is not None:
                q.enqueue(current.right)
            q.dequeue()