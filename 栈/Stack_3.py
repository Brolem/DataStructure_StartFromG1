'''使用栈反转字符串或链表'''

from Stack_1 import Stack

def Reverse(char, n):
    s =  Stack()
    for i in range(n):
        s.push(char[i])
    for i in range(n):
        char[i] = s.top_value()
        s.pop()
        
def Reverse_linkedlist():
    s = Stack()
    current = head
    while current is not None:
        s.push(current)
        current = current.next
    current = s.top_value()
    head = current
    s.pop()
    while current is not None:
        current.data = s.top_value()
        s.pop()
        current = current.next
    current.next = None
    
if __name__ == '__main__':
    char = list(input('Enter a string \n'))
    Reverse(char, len(char))
    for i in char:
        print(i, end='')