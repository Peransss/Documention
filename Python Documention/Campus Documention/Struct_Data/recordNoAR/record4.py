class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
        
x = int(input('\nJumlah Buah : '))

for i in range(x):
    Buah.nama = input('Nama : ')
    Buah.warna = input('Warna : ')
    Buah.rasa = input('Rasa : ')   
    print()


    