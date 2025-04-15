LuasL = []
KelilingL = []
LuasT = []
    
def Lingkaran():
    r =  int(input("Rusuk : "))
    Luas = 3.14 * r**2
    Keliling = 2 * 3.14 * r
    LuasL.append(Luas)
    KelilingL.append(Keliling)
        
def Trapesium():
    at = int(input("Alas Atas : "))
    ab = int(input("Alas Bawah : "))
    t = int(input("Tinggi : "))
    Luas = ((at + ab) * t) / 2
    LuasT.append(Luas)

def CetakData():
    c = input("Cetak Data : ")
    
    if c == "Lingkaran":        
        d = input("Apakah ingin menambahkan data kedalam file? (Y/N) : ")
        
        if d == "Y":
            a =  open("file1.txt", "w")
            a.write(f'Luas Lingkaran : {LuasL}')
            a.write(f'\nKeliling Lingkaran : {KelilingL}')
            a.close()
            print("Data berhasil dicetak pada file")
        elif d == "N":
            exit
            
        g = input("Apakah ingin mencetak data? (Y/N) : ")
        
        if g == "Y":
            j = open("file1.txt", "r")
            print(j.read())
        elif g == "N":
            exit
        
    if c == "Trapesium":
        l = input("Apakah ingin menambahkan data kedalam file? (Y/N) : ")
        
        if a == "Y":
            b = open("file1.txt", "w")
            b.write(f'Luas Trapesium : {LuasT}')
            b.close()
            print("Data berhasil dicetak pada file")
        elif a == "N":
            exit
            
        v = input("Apakah ingin mencetak data? (Y/N) : ")
        
        if v == "Y":
            m = open("file1.txt", "r")
            print(m.read())
        elif v == "N":
            exit            

def menu():  
    while True:  
        print("""====
Menu
====
1. Lingkaran
2. Trapesium
3. Cetak Data
4. Exit
====
Pilih
====""")
    
        n = (int(input("Menu : ")))
        
        if n == 1:
            Lingkaran()
        elif n == 2:
            Trapesium()
        elif n == 3:
            CetakData()
        elif n == 4: 
            break
        
menu()