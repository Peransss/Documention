class Pegawai:
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok):
        self.__id = id
        self.__nama = nama
        self.__status_kerja = status_kerja
        self.__jenis_kelamin = jenis_kelamin
        self.__status_menikah = status_menikah
        self.__jml_anak = jml_anak
        self.__gapok =  gapok
        
    @property
    def id1(self):
        return self.__id
    
    @id1.setter
    def id1(self, id):
        self.__id = id    
        
    @property
    def nama1(self):
        return self.__nama
    
    @nama1.setter
    def nama1(self, nama):
        self.__nama = nama
        
    @property
    def status_kerja1(self):
        return self.__status_kerja
    
    @status_kerja1.setter
    def status_kerja1(self, status_kerja):
        self.__status_kerja = status_kerja
        
    @property
    def jenis_kelamin1(self):
        return self.__jenis_kelamin 
    
    @jenis_kelamin1.setter
    def jenis_kelamin1(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin
        
    @property
    def status_menikah1(self):
        return self.__status_menikah
    
    @status_menikah1.setter
    def status_menikah1(self, status_menikah):
        self.__status_menikah = status_menikah
        
    @property
    def jml_anak1(self):
        return self.__jml_anak 
    
    @jml_anak1.setter
    def jml_anak1(self, jml_anak):
        self.__jml_anak = jml_anak
        
    @property
    def gapok1(self):
        return self.__gapok
    
    @gapok1.setter
    def gapok1(self, gapok):
        self.__gapok = gapok
        
class Pegawai_tetap(Pegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, lama_lembur, biaya_lembur_per_jam):
        super().__init__(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok)
        self.__lama_lembur = lama_lembur
        self.__biaya_lembur_per_jam = biaya_lembur_per_jam
        
    @property
    def lama_lembur1(self):
        return self.__lama_lembur
    
    @lama_lembur1.setter
    def lama_lembur1(self, lama_lembur):
        self.__lama_lembur = lama_lembur
        
    @property
    def biaya_lembur_per_jam1(self):
        return self.__biaya_lembur_per_jam 
    
    @biaya_lembur_per_jam1.setter
    def biaya_lembur_per_jam1(self, biaya_lembur_per_jam):
        self.__biaya_lembur_per_jam = biaya_lembur_per_jam
        
    def tunjangan(self):
        return self.gapok1 * 0.1
    
    def bonus(self):
        return self.gapok1 * 0.1
    
    def uang_lembur(self):
        return self.__lama_lembur * self.__biaya_lembur_per_jam
    
    def pph(self):
        return self.gapok1 * 0.015
    
    def thr(self):
        return self.gapok1
    
    def tun_istri(self):
        if self.jenis_kelamin1 == 'P' and self.status_menikah1 == 'M':
            return self.gapok1 * 0.3
        else:
            return 0
            
    def tun_anak(self):
        if self.status_menikah1 == 'M' and self.jml_anak1 > 3:
            return (self.gapok1 * 0.2) * 3
        elif self.status_menikah1 == 'M' and self.jml_anak1 <= 3:
            return self.jml_anak1 * (self.gapok1 * 0.2)
        else:
            return 0
            
    def total_gaji(self):
        return (self.tunjangan() + self.uang_lembur() + self.thr() + self.tun_anak() + self.gapok1) - self.pph()

class PegawaiKontrak(Pegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_prestasi):
        super().__init__(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok)
        self.__uang_prestasi = uang_prestasi
        
    @property
    def uang_prestasi1(self):
        return self.__uang_prestasi
    
    @uang_prestasi1.setter
    def uang_prestasi1(self, uang_prestasi):
        self.__uang_prestasi = uang_prestasi
        
    def bonus(self):
        return self.gapok1 * 0.1
    
    def tunjangan(self):
        return self.gapok1 * 0.1
    
    def pph(self):
        return self.gapok1 * 0.015

    def total_gaji(self):
        return (self.uang_prestasi1 + self.bonus() + self.tunjangan() + self.gapok1) - self.pph()

class Pegawaiharian(Pegawai):
    def __init__(self, id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_per_hari):
        super().__init__(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok)
        self.__uang_per_hari = uang_per_hari
        
    @property
    def uang_per_hari1(self):
        return self.__uang_per_hari
    
    @uang_per_hari1.setter
    def uang_per_hari1(self, uang_per_hari):
        self.__uang_per_hari = uang_per_hari
        
    def pph(self):
        return self.gapok1 * 0.015

    def total_gaji(self):
        return (self.uang_per_hari1 + self.gapok1) - self.pph()