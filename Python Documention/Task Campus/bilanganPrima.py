x = 2
y = int(input("Maks : "))

while x <= y:    
    n = 2
    
    isPrima = True
    
    while n <= x // 2:
        if x % n == 0:
            isPrima = False
            break
        n += 1
        
    if isPrima:
        print(x, end = " ")
   
    x += 1   
       
