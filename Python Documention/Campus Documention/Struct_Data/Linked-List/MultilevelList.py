class Node:
    def __init__(self):
        self.data = input('Node : ')
        self.next = None
        self.child = None
        
class MultilevelList:
    def __init__(self):
        self.head = None
        
    def addFirst(self):
        smp = Node()
        if self.head is None:
            self.head = smp
        else:
            smp.next = self.head
            self.head = smp
            
    def addNextNode(self):
        smp = Node()
        if self.head is None:
            print('Linked list is empty!')
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = smp
            
    def addChild(self):
        smp = Node()
        ptr = self.head
        if self.head:
            while ptr.next:
                ptr = ptr.next                
            ptr.child = smp
                
    def addNextChild(self):
        smp = Node()
        ptr = self.head
        if ptr.child:
            ptr = ptr.child
            while ptr.next:
                ptr = ptr.next
            ptr.next = smp
                 
    def display(self):
        if self.head is None:
            print('Linked List is none!')
        else:
            ptr = self.head
            ptr_c = ptr.child
            while ptr:
                print(ptr.data, end = ' >> ')
                if ptr.next is None:
                    print('None!')
                while ptr.child:
                    print('|')
                    print(ptr_c.data)
                    ptr_c = ptr_c.next
                    if ptr_c is None:
                        break
                ptr = ptr.next
        
mll = MultilevelList()
mll.addFirst()
mll.display()
mll.addChild()
mll.display()
mll.addNextChild()
mll.display()
