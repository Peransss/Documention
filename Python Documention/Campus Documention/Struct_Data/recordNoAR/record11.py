class Product:
    def __init__ (self):
        self.products_list = {'Name' : ' ',
                              'Price' : ' ',
                              'Quantity Available' : ' '}
        self.products_list1 = []

        n = int(input('Total Product : '))
        
        print('---\tInventory\t---')
        for i in range(n):
            self.name = input('Product : ')
            self.price1 = int(input('Price : '))
            self.quanAV = int(input('Quantity Available: '))
            
            self.products_list['Name'] = self.name
            self.products_list['Price'] =  self.price1
            self.products_list['Quantity Available'] = self.quanAV
            
            print()
                        
            self.products_list1.append(self.products_list)
            
    def checkingINV(self, name1, quanAV1):
        self.name1 = name1
        self.quanAV1 = quanAV1
        
        if self.name1 in self.products_list['Name']:
            print(f'Quantity Available : {self.quanAV}')
        elif self.quanAV1 is not None:
            if self.quanAV1 > self.products_list['Quantity Available'] :
                return 0
            return self.quanAV1 - self.quanAV
              
    def price(self):
        return self.price * self.quanAV
    
    def display_product(self):
        for i in range(len(self.products_list1)):
            print(self.products_list1[i]['Name']['Price'])
            print()
    
def main():
    prd = Product()
    
    print(f'\tGrosir Mall of Frans\t')
    print('-' * 30)
    print(prd.display_product())
    print('-' * 30)
    print('---\tSelect Product\t---')
    
    b = input('\nName Product\t: ')
    c = int(input('Quantity\t: '))
    
if __name__ == '__main__':
    main()