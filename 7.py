import random as rd

class Kendaraan:
    def __init__(self, plat, merk, tipe, tahun, status):
        self.__plat = plat
        self.merk = merk
        self.tipe = tipe
        self.tahun = tahun
        self.status = status
        
    @property
    def plat1(self):
        return self.__plat
    
    @plat1.setter
    def plat1(self, plat):
        self.__plat = plat

class RentalKen(Kendaraan):
    def __init__(self, plat, merk, tipe, tahun, status):
        super().__init__(plat, merk, tipe, tahun, status)
        chc = ['Tersedia', 'Tidak Tersedia']
        self.list = []
        self.status = rd.choice(chc)
                
    def tambahLST(self):
        self.list.append(Kendaraan(self.plat1, self.merk, self.tipe, self.tahun, self.status))
        
    def Lrental(self):
        for i in range(len(self.list)):
            print(self.list[i])
        
plat = input('Plat : ')
merk = input('Merk : ')
tipe = input('Tipe : ')
tahun = int(input('Tahun: '))

KND = Kendaraan(plat, merk, tipe, tahun, None)
RNTL = RentalKen(plat, merk, tipe, tahun, None)

RNTL.tambahLST()
RNTL.Lrental()

