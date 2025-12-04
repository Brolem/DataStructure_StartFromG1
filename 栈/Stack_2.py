'''使用链表实现栈'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
         
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.top is None:
            print("Error: No element to pop")
            return
        self.top = self.top.next   
    
    def top_value(self):
        if self.top is None:
            print("Error: Stack is empty")
            return None
        return self.top.data
    
    def print(self):
        """从栈底到栈顶打印栈内容"""
        if self.top is None:
            print("Stack is empty")
            return
        print("Stack:", end=' ')
        current = self.top
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        for data in reversed(elements):
            print(data, end=' ')
        print()
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(2); stack.print()
    stack.push(5); stack.print()
    stack.pop(); stack.print()
    print(stack.top_value())