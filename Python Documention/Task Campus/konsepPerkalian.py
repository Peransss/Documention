x = int(input("Perkalian : "))
y = int(input("Batas : "))
    
a = 1
    
while a <= y:
    print(f"Tabel Perkalian {x}")
    z =  x * a
    print(f"{x} * {a} = {z}")
    a += 1
    if a > y:
        break
        
                
    