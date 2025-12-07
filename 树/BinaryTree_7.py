'''BST的中序后继节点 case 1: node has right subtree 在右子树找最小的值,
                    case 2: no right subtree 在父节点向上找第一个左子树的节点'''
                    
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def find_min(node):
    if node is None: return None
    while node.left is not None:
        node = node.left
    return node
    
def find(node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return find(node.left, data)
        return find(node.right, data)    

def get_successor(node, data):
    # search the Node - O(h)
    current = find(node, data)
    if current is None: return None
    # case 1: node has right subtree
    if current.right is not None:
        return find_min(current.right)
    # case 2: no right subtree - O(h)
    else:
        successor = None
        ancestor = node
        while ancestor != current:
            if current.data < ancestor.data:
                successor = ancestor  # 记录可能的后继节点
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor