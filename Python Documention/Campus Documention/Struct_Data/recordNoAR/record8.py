
class Car:
    def __init__(self, mobil, BK):
        self.mobil = mobil 
        self.BK = BK
        
    def drive(self):
        km = float(input('KM : '))
        km1 = self.BK - (km * 0.1)
        print(f'Bahan Bakar Sisa : {km1}')
    
def main():
    mb = input('Mobil : ')
    BK = float(input('Bahan Bakar : '))
    
    a = Car(mb, BK)
    
    a.drive()
    
if __name__ == '__main__':
    main()