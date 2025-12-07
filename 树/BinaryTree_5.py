'''判断是非为BST'''

from 树.BinaryTree_1 import *

def is_subtree_lesser(node, value):
    if node is None: return True
    if node.data < value and \
       is_subtree_lesser(node.left, value) and \
       is_subtree_lesser(node.right, value):
        return True
    else:
        return False
        
def is_subtree_greater(node, value):
    if node is None: return True
    if node.data > value and \
       is_subtree_greater(node.left, value) and \
       is_subtree_greater(node.right, value):
        return True

def is_BST(node):
    """判断以 node 为根节点的二叉树是否为二叉搜索树"""
    if node is None: return True
    
    if is_subtree_lesser(node.left, node.data) and \
       is_subtree_greater(node.right, node.data) and \
       is_BST(node.left) and is_BST(node.right):
        return True
    else:
        return False
    
def is_BST_util(node, mini, maxi):
    """辅助函数：判断以 node 为根节点的二叉树是否为二叉搜索树"""
    if node is None: return True
    
    if node.data > mini and node.data < maxi and \
       is_BST_util(node.left, mini, node.data) and \
       is_BST_util(node.right, node.data, maxi):
        return True
    else:
        return False

def is_BST(node):
    return is_BST_util(node, float('-inf'), float('inf'))