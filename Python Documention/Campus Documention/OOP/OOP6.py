class Pegawai:
    def __init__(self, nama, tgl, alamat, gaji):
        self.__nama = nama
        self.__tgl = tgl
        self.__alamat = alamat
        self.__gaji = gaji

    @property
    def nama1(self):
        return self.__nama
    
    @nama1.setter
    def nama1(self, nama1):
        self.__nama = nama1
        
    @property
    def tgl1 (self):
        return self.__tgl
    
    @tgl1.setter 
    def tgl1 (self, tgl1):
        self.__tgl = tgl1
        
    @property
    def alamat1 (self):
        return self.__alamat
    
    @alamat1.setter 
    def alamat1 (self, alamat1):
        self.__alamat = alamat1       
        
    @property
    def gaji1 (self):
        return self.__gaji
            
    @gaji1.setter
    def gaji1 (self, gaji1):
        self.__gaji = gaji1
        
    def tunjangan(self):
        return self.__gaji * 0.15     

class Peg_Tetap(Pegawai):
    def __init__ (self, nama, tgl, alamat, gaji):
        super().__init__ (nama, tgl, alamat, gaji)   
        self.transpot = self.gaji1 * 0.05
        
    def totalgaji(self):
        return self.gaji1 + self.tunjangan() + self.transpot  
    
def main():
    a = input('Nama : ')
    g = input('Tanggal Lahir : ')
    j = input('Alamat : ')
    n = int(input('Gaji : '))    
    
    pgt = Peg_Tetap(a, g, j, n)
    
    print(f'Nama {pgt.nama1}',
          f'Tanggal Lahir {pgt.tgl1}',
          f'Alamat : {pgt.alamat1}',
          f'Total Gaji : {pgt.totalgaji()}')
    
if __name__ == '__main__':
    main()
    
    