'''从BST中删除一个节点 case 1: No child, case 2: One child, 
    case 3: Two children 在右子树找最小的值或在左子树找最大的值, 替换被删除节点, 转为case 1或case 2'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
def delete(root, data):
    if root is None: return root
    elif data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        # case 1: no child
        if root.left is None and root.right is None:
            del root
            root = None
        # case 2: one child
        elif root.left is None:
            temp = root
            root = root.left
            del temp
        elif root.right is None:
            temp = root
            root = root.right
            del temp
        # case 3: two children
        else:
            temp = find_min(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root

def find_min(root):
    if root is None:
        print("Error: Tree is empty")
        return root
    current = root
    while current.left is not None:
        current = current.left
    return current