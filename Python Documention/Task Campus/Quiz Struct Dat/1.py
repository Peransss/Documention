class Pasien:
    def __init__(self, id_pasien):
        self.id = id_pasien
        self.prev = None
        self.next = None
        
class AntrianPasien:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def tambah_pasien(self, id_pasien):
        smp = Pasien(id_pasien)
        ptr = self.head
        if self.head == None:
            self.head = smp
        else:
            ptr.next = smp
            smp.prev = ptr
            
    def hapus_pasien(self, id_pasien):
        ptr = self.head
        while ptr != id_pasien:
            ptr = ptr.next
        ptr.prev.next = ptr.next
        ptr = None
        
    def sisipkan_setelah(self, id_pasien_baru, target_id):
        smp = Pasien(id_pasien_baru)
        ptr = self.head
        pos_next = 0
        while ptr != None and pos_next + 1 == target_id:
            ptr = ptr.next
            pos_next += 1
            
        