class Makanan:
    def __init__(self, nama, harga, deskripsi):
        self.nama = nama
        self.harga = harga
        self.deskripsi = deskripsi

    def print_makanan(self):
        print(f"{self.nama} : Rp.{self.harga}")

class Minuman:
    def __init__(self, nama, harga, deskripsi):
        self.nama = nama
        self.harga = harga
        self.deskripsi = deskripsi
        
    def print_minuman(self):
        print(f"{self.nama} : Rp.{self.harga}")

class PaketMenu:
    def __init__(self, makanan, minuman, harga, harga_diskon):
        self.makanan = makanan
        self.minuman = minuman
        self.harga = harga
        self.harga_diskon = harga_diskon

    def print_menu(self):
        print("Paket Menu:")
        self.makanan.print_makanan()
        self.minuman.print_minuman()
        print(f"Harga Awal: Rp.{self.harga}")
        print(f"Harga Diskon: Rp.{self.harga_diskon}")
        selisih_harga = self.harga - self.harga_diskon
        print(f"Lebih murah: Rp.{selisih_harga}")

makanan1 = Makanan("Nasi Goreng", 17000, "Enak")
makanan2 = Makanan("Nasi Uduk", 12000, "Enak")
makanan3 = Makanan("Mie Goreng", 16000, "Enak")
makanan4 = Makanan("Kwetiaw Goreng", 16000, "Enak")
minuman1 = Minuman("Es Teh", 6000, "Segar")
minuman2 = Minuman("Es Jeruk", 10000, "Segar")
minuman3 = Minuman("Es Campur", 15000, "Segar")
minuman4 = Minuman("Es Buah", 15000, "Segar")

menu_combo1 = PaketMenu(makanan1, minuman1, 23000, 21000)
menu_combo2 = PaketMenu(makanan2, minuman2, 22000, 20000)
menu_combo3 = PaketMenu(makanan3, minuman3, 31000, 30000)
menu_combo4 = PaketMenu(makanan4, minuman4, 31000, 29000)

for menu_combo in [menu_combo1, menu_combo2, menu_combo3, menu_combo4]:
    menu_combo.print_menu()
    print("=" * 20)
    
soto = Makanan('Soto', 20000, 'Enak dan hangat untuk musim hujan')
gultik = Makanan('Gultik', 15000, 'Murah Meriah')
nasgor = Makanan('Nasi Goreng', 15000, 'Enak')
daftar_makanan = [soto, gultik, nasgor]

es_teh_manis = Minuman('Es Teh Manis', 5000, 'Es teh doang')
es_teh_tawar = Minuman('Es Teh Tawar', 4000, 'Cuma es teh biasa tanpa gula')
es_jeruk = Minuman('Es Jeruk', 6000, 'Segar')
daftar_minuman = [es_teh_manis, es_teh_tawar, es_jeruk]

paket1 = PaketMenu(nasgor, es_jeruk, 20000)
paket2 = PaketMenu(soto, es_teh_manis, 23000)
paket3 = PaketMenu(gultik, es_teh_tawar, 18000)
daftar_paket_menu = [paket1, paket2, paket3]

# 1 Tambahkan Ayam Goreng (Rp. 25.000)

ayamgoreng = Makanan('Ayam Goreng', 25000, 'Kriuk')
daftar_makanan.append(ayamgoreng)

# 2 Print daftar minuman dengan loop

for i in daftar_minuman:
    print(i.nama)
    
# 3 Menghapus Gultik dari daftar_makanan

daftar_makanan = [makanan for makanan in daftar_makanan if makanan.nama != 'Gultik']

# 4 Membuat array makanan_murah dengan list makanan di bawah RP. 20.000, lalu print

makanan_murah = [makanan for makanan in daftar_makanan if makanan.harga < 20000]
for i in makanan_murah:
    print(i.nama, i.harga)
    
# 5 Urutkan daftar paket menu berdasarkan harga

daftar_paket_menu.sort(key = lambda paket : paket.harga)
for i in daftar_paket_menu:
    print(i.makanan.nama, i.minuman.nama, i.harga)
    
# 6 Cari paket termurah di daftar paket menu

paket_termurah = min(daftar_paket_menu, key = lambda paket :paket.harga)
paket_termurah.print_menu()

# 7 Membuat sebuah array baru sebagai backup dari daftar paket menu, lalu mengosongkan

backup = daftar_paket_menu.copy()
daftar_paket_menu.clear()

daftar_paket_menu.append(soto, es_jeruk, 15000)
daftar_paket_menu.append(ayamgoreng, es_teh_manis, 20000)

# 8 Menggabungkan backup menu dan daftar paket menu

daftar_paket_menu.extend(backup)
for i in daftar_paket_menu:
    print(i.makanan.nama, i.minuman.nama, i.harga)
    
# 9 Hapus paket menu terakhir

daftar_paket_menu.pop()

# 10 Tambahkan paket menu baru (Nasi Goreng + Es Teh Tawar)Rp. 17.000, harga pada urutan 
daftar_paket_menu.insert(1, PaketMenu(nasgor, es_teh_tawar, 17000))