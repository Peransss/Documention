class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi
    
def main():
    panjang = int(input('Panjang : '))
    lebar = int(input('Lebar : '))
    tinggi = int(input('Tinggi : '))
    
    balok = Balok(panjang, lebar, tinggi)
    
    volume = float(balok.hitung_volume())
    
    print(f'Volume : {volume}')
    
if __name__ == '__main__':
    main()