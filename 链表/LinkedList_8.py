'''双向链表'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return f"Node({self.data})"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """在双向链表末尾添加新节点"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
    
    def display(self):
        """显示双向链表内容"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        #.join() 方法用于将序列中的元素以指定分隔符连接字符串列表
        return " <-> ".join(elements) + " <-> None"
    
    def __repr__(self):
        return self.display()
    
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(3)
    doubly_linked_list.append(5)
    print(doubly_linked_list)
    print(doubly_linked_list.display())