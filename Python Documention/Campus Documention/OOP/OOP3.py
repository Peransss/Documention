class Tabung:
    def __init__(self, jarijari, tinggi):
        self.jarijari = jarijari
        self.tinggi = tinggi
    
    def Volume(self):
        return 3.14 * (self.jarijari ** 2) * self.tinggi
    
# Mendeklarasi sebuah kelas Tabung
# Dengan Memiliki Atribut Jari-Jari & Tinggi
# Dimana atribut Jari-jari & tinggi akan diolah didalam suatu fungsi Volume
# Yang akan mengembalikan nilai setelah operasi aritmatika selesai
            
def main():
    print('Non Property Method')
    n = int(input('Jari-Jari : '))
    a = int(input('Tinggi : '))
    
    # User diminta input Jari-jari dan disetorkan value tersebut kedalam variable n
    # User diminta input Tinggi dan disetorkan value tersebut kedalam variable a
    
    c = Tabung(n, a)
    
    # Variable C akan menampung suatu nilai dari class Tabung dimana memiliki parameter n & a
    # Parameter n & a akan memenuhi parameter default yang sudah dicantumkan terlebih dahulu
    
    b = c.Volume()
    
    # Variable B akan menampung suatu nilai dari variable c dimana variable c menampung class Tabung
    # Dimana hanya memanggil fungsi Volume
    
    print(f'Volume Tabung : {b:.2f}')
    
if __name__ == '__main__':
    main()  
    
# Program akan dijalankan bila terdapat suatu fungsi bernama main
    
