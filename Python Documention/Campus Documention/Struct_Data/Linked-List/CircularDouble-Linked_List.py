class Node:
    def __init__(self):
        self.data = input('Data : ')
        self.prev = None
        self.next = None
        
class Double_Linked_List:
    def __init__(self):
        self.head = None
        
    def addFirst(self):
        smp = Node()
        if self.head is None:
            self.head = smp
            self.head.prev = None
            self.head.next = self.head
            
    def addNextNode(self):
        smp = Node()
        if self.head is None:
            print('Linked list is empty!')
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = smp
            smp.next = self.head
            smp.prev = ptr
            self.head.prev = smp
            
    def addMidNode(self, pos):
        ptr = self.head
        smp = Node()
        pos_next = 0
        if self.head is None:
            print('Linked list is empty!')
        else:
            while ptr != None and pos_next + 1 != pos :
                ptr = ptr.next
                pos_next += 1
            if pos_next <= 1:
                smp.next = ptr.next
                smp.prev = ptr
                ptr.next = smp
            else:
                ptr.next = smp
                smp.prev = ptr
                smp.next = self.head
   
    def addLast(self):
        ptr = self.head
        smp = Node()
        if self.head is None:
            print('Linked list is empty!')
        else:
            while ptr.next:
                if ptr.next == self.head:
                    break
                ptr = ptr.next
            if ptr.prev is not None and ptr.next is not None:
                ptr.next = smp
                smp.next = self.head
                smp.prev = ptr
                self.head.prev =  smp
            
    def removedFirst(self):
        ptr = self.head
        if self.head is None:
            print('Linked list is empty!')
        else:
            self.head = ptr.next
            
    def removedLast(self):
        ptr = self.head
        if self.head is None:
            print('Linked list is empty!')
        else:
            while ptr.next.next:
                ptr = ptr.next
            ptr.next = None
            
    def reverseLink(self):
        ptr = self.head
        prevNode = None
        if self.head is None:
            print('Linked list is empty!')
        else:
            while ptr is not None:
                prevNode = ptr.prev
                ptr.prev = ptr.next
                ptr.next = prevNode
                ptr = ptr.prev
            self.head = prevNode.prev
            
    def display(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            ptr = self.head
            while True:
                print(ptr.data, end = ' <<>> ')
                ptr = ptr.next
                if ptr == self.head:
                    print(ptr.data)    
                    break    
                    
dll = Double_Linked_List()
dll.addFirst()
dll.display()
dll.addNextNode()
dll.display()
dll.addNextNode()
dll.display()
dll.addLast()
dll.display()
dll.addMidNode(4)
dll.display()