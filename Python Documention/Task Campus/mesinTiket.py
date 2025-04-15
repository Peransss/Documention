y = 5000
print(f"Harga Tiket : {y}")
a = 0

while a < y:
    
    x = int(input("Uang : "))
      
    if x > y:
        x -= y
        print("Tiket berhasil dikeluarkan")
        print(f"Kembalian anda Rp {x}")
        break
      
    while x < y:
        y -= x
        print(f"Anda perlu memasukkan Rp {y} lagi")
        break
        
    if x == y:
        print("Tiket berhasil dikeluarkan")
        print("Tidak ada kembalian")
        break   
    
