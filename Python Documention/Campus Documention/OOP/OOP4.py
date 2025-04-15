from abc import ABC, abstractmethod

# Memanggil sebuah Library bernama ABC dimana memanggil abstractmethod

class abstrak_pegawai(ABC):
    @abstractmethod
    def tunjangan(self):
        pass
    
    @abstractmethod
    def bonus(self):
        pass
    
    @abstractmethod
    def total(self):
        pass
    
    # Akan mendeklarasikan sebuah superclass dimana memiliki turunan berupa class Pegawai
        
class Pegawai(abstrak_pegawai):
    def __init__(self, __id, __nama, __gaji):
        self.__id = __id
        self.__nama = __nama
        self.__gaji = __gaji
      
    # Atribut id, nama & gaji akan dideklarasikan dalam bentuk private 
    # Dimana hanya didalam class tersebut yang memiliki akses
        
    @property
    def id(self):
        return self.__id
    
    # @property ditandakan sebagai get
    # Dimana get ingin membaca nilai dari __id
    # Dengan menggunakan @property akan memberikan akses untuk mengakses variable dalam bentuk private

    @id.setter
    def id(self, id):
        self.__id = id
        
    # @id.setter ditandakan sebagai set
    # Dimana get ingin menulis nilai dari __id
        
    @property
    def nama(self):
        return self.__nama
    
    @nama.setter
    def nama(self, nama):
        self.__nama = nama
        
    @property
    def gaji(self):
        return self.__gaji
    
    @gaji.setter
    def gaji(self, gaji):
        self.__gaji = gaji
        
    def tunjangan(self):
        return self.__gaji * 0.05
    
    def bonus(self):
        return self.__gaji * 0.1
    
    def total(self):
        return self.__gaji + self.tunjangan() + self.bonus() 
    
    # Fungsi Tunjangan, bonus, total akan mengambil nilai dari __gaji
    # Dimana akan mengelolahnya untuk mengembalikan nilai berdasarkan operasi aritmatika setiap fungsinya
    
def main():
    while True:
        id_pegawai1 = int(input('Id \t: '))
        if id_pegawai1 == 0:
            print('Tidak ada input!')
        break
        
    nama_pegawai1 = input('Nama \t: ')
    
    while True:
        gaji_pegawai1 = int(input('Gaji \t: '))
        if gaji_pegawai1 == 0:
            print('Tidak ada input!')
        break
        
    dt_pegawai = Pegawai(id_pegawai1, nama_pegawai1, gaji_pegawai1)
    
    print('-' * 45)
    print(f'Id\t\t: {dt_pegawai.id}')
    print(f'Nama\t\t: {dt_pegawai.nama}')
    print(f'Gaji\t\t: Rp{dt_pegawai.gaji:.2f}')
    print(f'Tunjangan\t: Rp{dt_pegawai.tunjangan():.2f}')
    print(f'Bonus\t\t: Rp{dt_pegawai.bonus():.2f}')
    print(f'Total\t\t: Rp{dt_pegawai.total():.2f}')
    
main()