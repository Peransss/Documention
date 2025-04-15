class Node:
    def __init__(self):
        self.data = input('Node : ')
        self.next = None
        
class LinkedListStack:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def topEL(self):
        print(self.head.data) 
    
    def push(self):
        smp = Node()
        if self.head:
            smp.next = self.head
        self.head = smp
        
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
               
    def display(self):
        if self.head is None:
            print('Linked List is none!')
        else:
            ptr = self.head
            while True:
                print(ptr.data, end = ' >> ')
                if ptr.next is None:
                    print('None!')
                    break
                else:
                    ptr = ptr.next                

        
lls = LinkedListStack()

lls.push()
lls.display()
lls.push()
lls.display()
lls.push()
lls.display()
lls.pop()
lls.display()