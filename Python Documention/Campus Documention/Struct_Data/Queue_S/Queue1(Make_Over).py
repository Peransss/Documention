class Queue:
    def __init__ (self, max):
        self.data = [None] * max
        self.max = max
        self.first = -1
        self.last = -1
        self.size = 0
        
    def isEmpty(self):
        return self.first == -1
                
    def enQueue(self):
        dat = input('Data : ')
        if self.isEmpty():
            self.first = self.last = 0  
            self.data[self.last] = dat
            self.size += 1
        else:
            if self.size == self.max:
                print('Queue is full!')
            else:
                if self.first is not None:
                    self.last = (self.first + self.size) % self.max
                    self.data[self.last] = dat
                    self.size += 1
                else:
                    if self.data[(self.first + 1) % self.max] is None:
                        self.last = (self.first + self.size) % self.max
                        self.data[self.last] = dat
                        self.size += 1
                                     
    def deQueue(self):
        if self.isEmpty():
            print('Queue is empty!')
        else:
            if self.first == self.last:
                self.data[self.last] = None
                self.first = self.last = -1
                self.size -= 1
            else:
                self.data[self.first] = None
                self.first = (self.first + 1) % self.max
                self.size -= 1
                
    def isFirst(self):
        print(self.data[self.first])
        
    def isLast(self):
        print(self.data[self.last])
                    
q = Queue(4)
for i in range(4):
    q.enQueue()
q.deQueue()
q.enQueue()
q.enQueue()
q.deQueue()
q.isFirst()
q.isLast()
print(q.data)
