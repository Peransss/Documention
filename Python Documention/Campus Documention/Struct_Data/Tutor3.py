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
    
    def isFUll(self):
        return self.top == self.ukuran
    
    def push(self, el):
        if self.isFUll():
            print('Stack overflow!')
        else:
            self.data[self.top] = el
            self.top += 1
                    
    def pop(self):
        self.top -= 1
        temp = self.data[self.top]
        self.data[self.top] = 0
        return temp
        
    def display(self):
        print(self.data)
        
    def top1(self):
        return self.data[self.top - 1]
        
arr = [15, 7, 20, 3, 0]
s1 = stackPool([], len(arr))

for i in arr:
    s1.push(i)
    
s1.display()

s2 = stackPool([], len(arr))

def sort(s1, s2):
    s3 = stackPool([], len(arr))
    while not s1.isEmpty():
        temp = s1.pop()
        while not s3.isEmpty():
            top_el = s3.top1()
            if temp > top_el:      
                s1.push(s3.pop())
            else:
                break
                 
        s3.push(temp)     
        
    while not s3.isEmpty():
        s2.push(s3.pop())
        
sort(s1, s2)
s2.display()

s_genap = stackPool([], len(arr))
s_ganjil = stackPool([], len(arr))

while not s2.isEmpty():
    temp = s2.pop()
    if temp % 2 == 0:
        s_genap.push(temp)
    else:
        s_ganjil.push(temp)
        
s_genap.display()
s_ganjil.display() 