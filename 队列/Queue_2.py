'''使用链表实现队列'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next   
        
    def print(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        print("Queue:", end='')
        current = self.front
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
        
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5) 
    queue.enqueue(7); queue.print()
    queue.dequeue(); queue.print()
    queue.enqueue(12)
    queue.dequeue(); queue.print()