class Queue:
    def __init__(self, max):
        self.data = [None] * max
        self.max = max
        self.size = 0
        self.first = self.last = -1
        
    def isEmpty(self):
        return self.first == -1
        
    def enQueue(self, dat):
        if self.isEmpty():
            self.first = self.last = 0
            self.data[self.last] = dat
            self.dat = dat
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
            return self.data[self.last]

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
        return self.data[self.first]
                
    def isFirst(self):
        return self.data[self.first]
        
    def isLast(self):
        return self.data[self.last]
        

q1 = Queue(10)
q2 = Queue(10)
a = [77, 23, 50, 45, 5, 10, 73, 0]
arr = []

for i in a:
    q1.enQueue(a)

while not q1.isEmpty():
    num = 0
    sum = 0
    while q1.isFirst() % 2 != 0:
        q2.enQueue(q1.deQueue())
        a = q2.enQueue(q1.deQueue())
        num += 1
        sum += a
    b = sum / num
    arr.append(b)
    while not q2.isEmpty():
        q1.enQueue(q2.deQueue())
    