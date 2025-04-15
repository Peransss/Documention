class Node:
    def __init__(self):
        self.data = input('Data : ')
        self.next = None
        
class CircularLL:
    def __init__(self):
        self.head = None
        
    def addFirst(self):
        smp = Node()
        self.head = smp
        self.head.next = self.head
        
    def addNextNode(self):
        ptr = self.head
        smp = Node()
        if self.head is None:
            print('Linked List is empty!')
        else:
            while ptr.next != self.head:
                ptr = ptr.next
            smp.next = self.head
            self.head = smp
            ptr.next = self.head
            
    def addMidNode(self, pos):
        ptr = self.head
        smp = Node()
        pos_next = 0
        if self.head is None:
            print('Linked List is empty!')
        else:
            while ptr != None and pos_next + 1 != pos:
                ptr = ptr.next
                pos_next += 1
            if ptr.next:
                smp.next = ptr.next
                ptr.next = smp
    
    def display(self):
        if self.head is None:
            print('Linked List is none!')
        else:
            ptr = self.head
            while True:
                print(ptr.data, end = ' >> ')
                ptr = ptr.next
                if ptr == self.head:
                    print(ptr.data)
                    break
                
cll = CircularLL()
cll.addFirst()
cll.addNextNode()
cll.addMidNode(1)
cll.display()

            
        