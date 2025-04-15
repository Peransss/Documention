class mahasiswa:
    def __init__(self):
        self.nama = str(input('Nama : '))
        self.umur = int(input('Umur : '))
        self.nilai = []
        
    def tambah_nilai(self):
        score = int(input('Nilai : '))
        self.nilai.append(score)
        
    def rata_rata(self):
        return sum(self.nilai) / len(self.nilai)
        
dtMHS = mahasiswa()

while True:
    dtMHS.tambah_nilai()
    x = input('Apakah ingin tambah? [Y/N] : ')
    
    if x == 'Y':
        continue
    else:
        print(f'Rata-rata : {dtMHS.rata_rata()} ')
        break
    