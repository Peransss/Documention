from abc import ABC, abstractmethod

class ABPegawai(ABC):
    @abstractmethod
    def tunjangan(self):
        pass
    
    @abstractmethod
    def bonus(self):
        pass
    
    @abstractmethod
    def uanglembur(self):
        pass
    
    @abstractmethod
    def pph(self):
        pass
    
    @abstractmethod
    def thr(self):
        pass
    
    @abstractmethod
    def tun_istri(self):
        pass
    
    @abstractmethod
    def tun_anak(self):
        pass
    
    @abstractmethod
    def total_gaji(self):
        pass
    
class Pegawai(ABPegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok):
        self.id = id
        self.nama = nama
        self.status_kerja = status_kerja
        self.jenis_kelamin = jenis_kelamin
        self.status_menikah = status_menikah
        self.jml_anak = jml_anak
        self.gapok = gapok
        
class PegawaiTetap(Pegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, lama_lembur, biaya_lembur_per_jam):
        super().__init__(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok)
        self.lama_lembur = lama_lembur
        self.biaya_lembur_per_jam = biaya_lembur_per_jam
        
    def tunjangan(self):
        return self.gapok * 0.1
    
    def bonus(self):
        return self.gapok * 0.1
    
    def uanglembur(self):
        return self.lama_lembur * self.biaya_lembur_per_jam
    
    def pph(self):
        return self.gapok * 0.015
    
    def thr(self):
        return self.gapok
    
    def tun_istri(self):
        if self.jenis_kelamin == 'P' and self.status_menikah == 'M':
            return self.gapok * 0.3
        else:
            return 0
        
    def tun_anak(self):
        if self.status_menikah == 'M' and self.jml_anak > 3:
            return (self.gapok * 0.2) * 3
        elif self.status_menikah == 'M' and self.jml_anak <= 3:
            return (self.gapok * 0.2) * self.jml_anak
        else:
            return 0
        
    def total_gaji(self):
        return (self.tunjangan() + self.bonus() + self.uanglembur() + self.thr() + self.tun_istri() + self.tun_anak() + self.gapok) - self.pph()

class PegawaiKontrak(Pegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_prestasi):
        super().__init__(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_prestasi)
        self.uang_prestasi = uang_prestasi
        
    def tunjangan(self):
        return self.gapok * 0.1
    
    def bonus(self):
        return self.gapok * 0.1
    
    def pph(self):
        return self.gapok * 0.015
    
    def total_gaji(self):
        return (self.uang_prestasi + self.bonus() + self.tunjangan()) - self.pph()
    
class PegawaiHarian(Pegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_per_hari):
        super().__init__(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok)
        self.uang_per_hari = uang_per_hari
        
    def pph(self):
        return self.gapok * 0.015
    
    def total_gaji(self):
        return (self.uang_per_hari + self.gapok) - self.pph()