class orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def display(self):
        print(f'Nama : {self.nama}\nUmur : {self.umur}')
        
    def update_nama(self, nama):
        self.nama = nama
        return self.nama
    
    def update_umur(self, umur):
        self.umur = umur
        return self.umur
        
a = orang('Babo', '9')
a.display()
a.update_nama('Cendy')
a.update_umur('15')
a.display()
