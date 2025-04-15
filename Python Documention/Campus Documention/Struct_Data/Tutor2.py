class Menu:
    def __init__(self):
        self.makanan = str(input("Makanan :"))
        self.minuman = str(input("Minuman :"))
        self.harga = int(input("Harga :"))
        self.deskripsi = str(input("Deskripsi :"))

    def display(self):
        print(f"{self.makanan} : {self.harga}")
        print(f"{self.minuman} : {self.harga}")
        
class PaketMenu:
    def __init__(self, makanan, minuman, harga, harga_diskon,selisih_harga):
        self.makanan = makanan
        self.minuman = minuman
        self.harga = harga
        self.harga_diskon = harga_diskon
        self.selisih_harga = selisih_harga

print(PaketMenu)