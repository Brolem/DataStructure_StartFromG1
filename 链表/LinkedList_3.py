'''链表：任意插入节点'''
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
    
    # 任意插入函数
    def insert(self, data, n):
        """data: 插入数据
           n: 插入位置(从1开始)"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        if n == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(n - 2):
            if current.next is None:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
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

# 分离接口和实现；当被导入时只提供功能，不执行测试
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(2,1)
    linked_list.insert(3,2)
    linked_list.insert(4,3)
    linked_list.insert(1,6)
    linked_list.insert(5,2)
    print(linked_list)
