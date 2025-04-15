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
        else:            
            if self.last == self.max - 1 and self.first == 0 or self.first == self.last + 1:
                  print('Queue is full')
            else:
                if self.last != self.max - 1:
                    self.last += 1
                    self.data[self.last] = dat
                else:
                    self.last = 0
                    self.data[self.last] = dat
                            
    def deQueue(self):
        if self.isEmpty():
            print('Queue is empty!')
        else:
            if self.first == self.last:
                self.data[self.last] = None
                self.first = self.last = -1
            else:
                self.data[self.last] = None
                self.last -= 1
                    
q = Queue(4)
for i in range(4):
    q.enQueue()
print(q.data)