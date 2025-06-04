class Node:
    def __init__(self):
        self.data = input('Node : ')
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None 
        
    def addFirst(self):
        smp = Node()
        if self.head is None:
            self.head = smp
        else:
            smp.next =  self.head
            self.head = smp
            
    def addLast(self):
        smp = Node()
        if self.head is None:     
            self.head = smp
        else: 
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = smp   
            
    def removedFirst(self):
        if self.head is None:
            print('Linked List is none!')
        elif self.head.next == None:
            self.head = None
        else:
            ptr = self.head
            self.head = self.head.next
            ptr.next = None
            
    def removedLast(self):
        ptr = self.head
        if self.head is None:
            print('Linked List is none!')
        else:
            ptr = self.head
            while ptr.next.next:
                ptr = ptr.next
            ptr.next = None
            
    def removedMid(self, pos):
        ptr = self.head
        pos_next = 0
        if pos == 0:
            if ptr.next:
                self.head = ptr.next
            else:
                self.head = None
        else:
            while ptr != None and pos_next + 1 != pos:
                ptr = ptr.next
                pos_next += 1
            if ptr:
                if ptr.next.next is None:
                    ptr.next = None
                else:
                    ptr.next = ptr.next.next
            else:
                print('Cant be remove!')
                
    def insertMid(self, pos):
        ptr = self.head
        pos_next = 0
        if pos == 0:
            self.addFirst()
        elif pos_next + 1 == pos:
            while ptr != None and pos_next + 1 != pos:
                ptr = ptr.next
                pos_next += 1
            smp = Node()
            if ptr.next:
                smp.next = ptr.next
                ptr.next = smp
            if ptr != None:
                ptr.next = smp
                pos_next += 1
            else:
                print('Data cant be insert!')
                
    def addNextNode(self):
        smp = Node()
        if self.head is None:
            print('Linked list is empty!')
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = smp
            
    def reverseLink(self):
        ptr = self.head
        temp = None
        if self.head is None:
            print('Linked list is empty!')
        else:
            while ptr:
                nextN = ptr.next
                ptr.next = temp
                temp = ptr
                ptr = nextN
            self.head = temp
            
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
        
ll = linkedlist()

ll.addFirst()
ll.addNextNode()
ll.addNextNode()
ll.reverseLink()
ll.display()
