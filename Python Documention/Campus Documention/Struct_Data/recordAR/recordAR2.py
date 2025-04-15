class Book:
    def __init__(self):
        self.title = str(input('Judul : '))
        self.pub = str(input('Penulis : '))
        self.year = int(input('Tahun Terbit : '))
        
    def addColl(self):
        self.Coll = []
        self.DicDT = {'Judul' : ' ',
                      'Publisher' : ' ',
                      'Year' : ' '}
        
        self.n = int(input('Jumlah Buku : '))
        for i in range(self.n):
            self.Coll.append(Book())
            
    def display(self):
        print('NO', 'Buku', 'Publisher', 'Year', sep = '\t| ', end = '\n-----------------------------\n')
        for a in range(self.n):
                
        
book = Book()
print(book.title, book.pub, book.year)