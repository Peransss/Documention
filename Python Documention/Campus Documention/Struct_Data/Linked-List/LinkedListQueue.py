class Node:
    def __init__(self):
        self.data = input('Node : ')
        self.prev = None
        self.next = None
        
class LinkedListQueue:
    def __init__(self):
        self.head = None
        
    def enQueue(self):
        smp = Node()
        ptr = self.head
        if self.head is None:
            self.head = smp
        else:
            if self.head.next is None:
                self.head.next = smp
                smp.prev = self.head
            else:
                while ptr.next:
                    ptr = ptr.next
                ptr.next = smp
                smp.prev = ptr
                     
    def deQueue(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            
    def display(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            ptr = self.head
            while True:
                print(ptr.data, end = ' <<>> ')
                if ptr.next is None:
                    print('None')    
                    break    
                else:
                    ptr = ptr.next

llq = LinkedListQueue()
llq.enQueue()
llq.display()
llq.enQueue()
llq.display()
llq.enQueue()
llq.display()
llq.enQueue()
llq.display()
llq.deQueue()
llq.display()