class BA:
    def __init__(self, nama, saldo, rek):              
        self.nama =  nama
        self.saldo = saldo
        self.rek = rek
                
    def MTSaldo(self, MTSPlus, MTSMin):
        self.MTSPlus = MTSPlus
        self.MTSMin = MTSMin      
                
def main():
    x = str(input('Apakah ada Belanja? [Y/N] : '))
    
    dataACC = []
    dataACC1 = {'Nama' : ' ',
                'Saldo' : ' ',
                'Rek' : ' '}

    if x == 'Y':    
        dataACC1['Nama'] = str(input('Nama : '))
        dataACC1['Saldo'] = int(input('Saldo : '))
        dataACC1['Rek'] = int(input('Rek : '))
    else:
        print('Tidak ada pengeluaran!')
        
if __name__ == '__main__':
    main()