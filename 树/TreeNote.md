### Applications

1. Storing naturally
    hierarchical data -> eg. **file system**
2. Organize data
    for quick search, insertion, deletion -> eg **Binary Search trees**
3. Trie -> **dictionary**
4. Network Routing algorithm


### Binary Tree

1. 完全二叉树左对齐
2. 完美二叉树所有层级都被填满
3. 平衡二叉树的左右子树高度差 <= 1
4. 最大结点数 n = 2^h+1^-1
5. min_height = log~2~n **O(log~2~n)**, max_height = n-1 **O(n)**
6. Height of an empty tree = -1,Height of tree with 1 node = 0
7. diff = |h~left~ - h~right~| 完美树的所有结点diff都是0
8. 区分：**深度**是到根节点的距离，**高度**是到最深叶节点的距离


### Binary Search Tree

左子树的值比根节点更小，右子树的值比根节点更大

- | Array (unsorted) | Linked List | Array (sorted) | BST
------- | ------ | ------ | ------ | ------
Search(x) | O(n) | O(n) | O(log~2~n) | O(log~2~n)
Insert(x) | O(1) | O(1) | O(n) | O(log~2~n)
Remove(x) | O(n) | O(n) | O(n) | O(log~2~n)


### 二叉树的遍历

1. **广度优先**(Breadth-first): Level-order
   1. Time-Complexity = O(n)
   2. Space-Complexity O(1)-best O(n)-worst
2. **深度优先**(Depth-first): 
    1. (root)(left)(right) - Pre-order 
    2. (left)(root)(right) - In-order
    3. (left)(right)(root) - Post-order