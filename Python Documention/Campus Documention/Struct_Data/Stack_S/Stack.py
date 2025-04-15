class stackPool:
    def __init__ (self, data, ukuran):        
        self.data = data
        for i in range(ukuran):
            self.data.append(0)
        self.ukuran = ukuran
        self.top = 0 
        
    def clearStack(self):
        self.ukuran = 0
        
    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.top == self.ukuran - 1
    
    def push(self, el):
        self.top += 1
        self.data[self.top - 1] = el  
        
    def pop(self):
        self.top -= 1
        temp = self.data[self.top]
        self.data[self.top] = 0
        return temp
        
    def display(self):
        print(self.data)
        
    def top1(self):
        print(self.data[self.top - 1])
        
ukr = int(input('Ukuran : '))
pool = stackPool([], ukr)
i = 0

while True:
    dat = int(input('Data : '))
    pool.push(dat)
    i += 1
    
    if i == ukr:
        break
    
pool.display()
pool.clearStack()


      