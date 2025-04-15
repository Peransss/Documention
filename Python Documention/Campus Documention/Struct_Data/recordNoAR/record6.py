class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def Luas(self):
        return self.length * self.width

    def Keliling(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        print(f'Luas : {self.Luas()}\nKeliling : {self.Keliling()}')
        
p = float(input('Panjang \t: '))
l = float(input('Lebar \t: '))

pl = Rectangle(p, l)
pl.display()
