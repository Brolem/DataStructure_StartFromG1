'''反转链表（迭代）'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        '''f 在这里表示 f-string(格式化字符串字面值)'''
        #return "Node({})".format(self.data)
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
    
    # 尾部插入函数
    def append(self, data):
        """在链表末尾添加新节点"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def reverse_iteration(self):
        """反转链表"""
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  # 保存下一个节点
            current.next = prev       # 反转当前节点的指针
            prev = current            # 移动 prev 和 current 指针
            current = next_node
        
        self.head = prev  # 更新头指针为新的头节点
    
    #显示函数
    def display(self):
        """显示链表内容"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        #.join() 方法用于将序列中的元素以指定分隔符连接字符串列表
        return " -> ".join(elements) + " -> None"
    
    def __repr__(self):
        return self.display()

# 被导入时只提供功能，不执行测试；分离接口和实现
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(6)
    print(linked_list.display())
    linked_list.reverse_iteration()
    print(linked_list.display())
