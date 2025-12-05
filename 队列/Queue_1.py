'''使用数组实现队列'''

MAX_SIZE = 10

class Queue:
    def __init__(self):
        self.A = [0] * MAX_SIZE
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
    
    def is_full(self):
        if self.rear == MAX_SIZE - 1:
            return True
        else:
            return False
        
    def enqueue(self, x):
        if self.is_full():
            return
        elif self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        
        self.A[self.rear] = x  
        
    def enqueue_circle(self, x):
        if (self.rear + 1) % MAX_SIZE == self.front:
            return
        elif self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % MAX_SIZE
        self.A[self.rear] = x
        
    def dequeue(self):
        if self.is_empty():
            return
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1 
            
    def dequeue_circle(self):
        if self.is_empty():
            return 
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % MAX_SIZE 
        
    def print(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue:", end=' ')
        for i in range(self.front, self.rear + 1):
            print(self.A[i], end=' ')
        print()    
    
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5) 
    queue.enqueue(7); queue.print()
    queue.dequeue(); queue.print()