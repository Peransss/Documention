class Tabung1:
    def __init__(self, __jarijari1, __tinggi1):
        self.__jarijari1 = __jarijari1
        self.__tinggi1 = __tinggi1
    
    @property
    def Diameter1(self):
        return self.__jarijari1
    
    # @property ditandakan sebagai get
    # Dimana get ingin membaca nilai dari __jarijari1
    # Dengan menggunakan @property akan memberikan akses untuk mengakses variable dalam bentuk private

    @Diameter1.setter
    def Diameter1(self, __jarijari1):
        self.__jarijari1 = __jarijari1
        
    # @Diameter1.setter ditandakan sebagai set
    # Dimana set ingin menulis nilai dari __jarijari1
            
    @property
    def Tinggi1(self):
        return self.__tinggi1

    @Tinggi1.setter
    def Tinggi1(self, __tinggi1):
        self.__tinggi1 = __tinggi1
        
    def Volume1(self):
        return 3.14 * (self.__jarijari1 ** 2) * self.__tinggi1
    
    # Nantinya saat @property & @---.setter selesai melakukan tugasnya untuk membaca dan menulis nilai
    # Maka akan dilakukan operasi aritmatika didalam fungsi Volume1
    
def main():
    print('Property Method')
    f = float(input('Jari-jari : '))
    d = float(input('Tinggi : '))
    
    g = Tabung1(f, d)
    
    # Variable G akan menampung class Tabung dengan memiliki parameter
    # Dimana akan menjadi suatu nilai setelah proses dalam class tersebut selesai
    
    print(f'Volume Tabung : {g.Volume1():.2f}')
    
if __name__ == '__main__':
    main()
    
# Program akan dijalankan bila terdapat fungsi main

