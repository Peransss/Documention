class Node:
    def __init__(self):
        self.data       = input("Input data: ")
        self.previous   = None
        self.next       = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAwal(self):
        new_node = Node()
        if self.head is None:
            self.head = self.tail = new_node # head dan tail adalah simpul baru
        else:
            new_node.next       = self.head # next link simpul baru ke head
            self.head.previous  = new_node  # prev link head ke simpul baru
            self.head           = new_node  # set head baru adalah simpul baru
            self.head.next      = self.head
            
    def insertTengah(self):
        new_node = Node()
        if self.head is None:
            print("Double Linked List kosong. Tidak bisa insert di posisi tersebut")
        else:
            posisi = int(input("Input Posisi Current Cell : "))
            if posisi == 0:
                print("Silakan panggil fungsi insertAwal")
            elif posisi > 0:
                ptr     = self.head # current
                index   = 0  # flag posisi current node
                
                while (ptr.next!=self.head) and (index!=posisi):
                    ptr = ptr.next
                    index+=1
                
                if(index == posisi):
                    if(ptr.next==None): # insert di posisi akhir
                        print("Silakan panggil fungsi insertAkhir")                                                
                    else: # insert di posisi tengah
                        letak  = int(input("Input Letak [1:setelah current cell; 0:sebelum]: "))
                        if letak==1: # setelah current cell
                            new_node.next       = ptr.next      # next link simpul baru ke next link current
                            new_node.previous   = ptr           # prev link simpul baru ke current
                            ptr.next.previous   = new_node      # prev link setelah current ke simpul baru
                            ptr.next            = new_node      # next link current ke simpul baru
                        elif letak==0: # sebelum current cell
                            new_node.previous   = ptr.previous  # prev link simpul baru ke prev link current
                            new_node.next       = ptr           # next link simpul baru ke current
                            ptr.previous.next   = new_node      # next link sebelum current ke simpul baru
                            ptr.previous        = new_node      # prev link current ke simpul baru
                        else:
                            print("Tidak ada pilihan letak tersebut.")
                else:
                    print("Posisi yang diinput tidak ditemukan.")
            else:
                print("Posisi yang diinput tidak ditemukan.")
    
    def insertAkhir(self):
        ptr = self.head
        new_node = Node()
        if self.head is None:
            print("Double Linked List kosong. Tidak bisa insert di posisi tersebut")
        else:
            while ptr.next is not None:
                ptr = ptr.next
            new_node.previous   = self.tail # prev link simpul baru ke tail
            self.tail.next      = self.head  # next link tail ke simpul baru
            self.tail           = new_node  # set tail baru adalah simpul baru
            self.tail.prev      = ptr
    
    def searchMaju(self):
        if self.head is None:
            print("Double Linked List kosong.")
        else:
            cari    = input("Input data yang ingin dicari: ")
            ptr     = self.head
            index   = 0 
            while (ptr.next!=None) and (ptr.data!=cari):
                ptr = ptr.next
                index+=1
            if ptr.data == cari:
                print(f"Data '{cari}' ditemukan didalam double linked list pada posisi {index}")
            else:
                print(f"Data '{cari}' tidak ditemukan di dalam double linked list")
    
    def searchMundur(self):
        if self.head is None:
            print("Double Linked List kosong.")
        else:
            cari    = input("Input data yang ingin dicari: ")
            ptr     = self.tail 
            index   = self.count_nodes()-1
            while (ptr.previous!=None) and (ptr.data!=cari):
                ptr = ptr.previous
                index-=1
            if ptr.data == cari:
                print(f"Data '{cari}' ditemukan didalam double linked list pada posisi {index}")
            else:
                print(f"Data '{cari}' tidak ditemukan di dalam double linked list")
    
    def count_nodes(self):
        if self.head is None:
            count = 0
        else:
            ptr = self.head
            count = 1
            while ptr.next is not None:
                count+=1
                ptr = ptr.next
        return count
    
    def deleteAwal(self):
        if self.head is None:
            print("Double Linked List kosong.")
        else:
            ptr = self.head
            if (ptr.next==None) and (ptr.previous==None): #jika hanya 1 data saja dalam list
                self.head = None
                self.tail = None
            else:
                self.head           = ptr.next
                self.head.previous  = None
            print("Delete Node Awal Berhasil")
    
    def deleteTengah(self):
        if self.head is None:
            print("Double Linked List kosong.")
        else:
            posisi = int(input("Input posisi data yang ingin dihapus: "))
            if posisi==0:
                print("Silakan panggil fungsi deleteAwal")
            elif posisi>0:
                ptr     = self.head # current
                index   = 0  # flag posisi current node
                
                while (ptr.next!=self.head) and (index!=posisi):
                    ptr = ptr.next
                    index+=1
                
                # Penyesuaian referensi next dan previous      
                if(index == posisi):
                    if(ptr.next==None): # insert di posisi akhir
                        print("Silakan panggil fungsi deleteAkhir") 
                    else: # delete di posisi tengah
                        ptr.next.previous = ptr.previous
                        ptr.previous.next = ptr.next
                else:
                    print("Posisi yang diinput tidak ditemukan.")
            else:
                print("Posisi yang diinput tidak ditemukan.")
                
    
    def deleteAkhir(self):
        if self.head is None:
            print("Double Linked List kosong.")
        elif (self.head.next==None) and (self.head.previous==None): #jika hanya 1 data saja dalam list
            self.head = None
            self.tail = None
            print("Delete Node Akhir Berhasil")
        else:
            ptr             = self.tail
            self.tail       = ptr.previous
            self.tail.next  = None
            print("Delete Node Akhir Berhasil")
    
    def display(self):
        print(f"Isi Double Linked List Saat Ini: ",end="")
        if self.head: 
            ptr = self.head
            print("None <- ", end="")
            while ptr:
                print(ptr.data,end="")
                ptr = ptr.next
                if (ptr!=None):
                    print(" <=> ",end="")
                else:
                    print(" -> None")
                if ptr == self.head:
                    break
        else:
            print("Kosong")

dl = DoubleLinkedList()
dl.insertAwal()
dl.display()
dl.insertAwal()
dl.display()
dl.insertTengah()
dl.display()
dl.insertAkhir()
dl.display()

dl.searchMaju()
dl.searchMundur()

dl.deleteAwal()
dl.display()
dl.deleteTengah()
dl.display()
dl.deleteAkhir()
dl.display()
dl.deleteAwal()
dl.display()